from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['fullname', 'username', 'password', 'email']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already in use.")
        return value

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("Password must be at least 6 characters long.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class TokenObtainPairSerializer(serializers.Serializer):
    usernameOrEmail = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        identifier = data.get('usernameOrEmail')
        password = data.get('password')

        if '@' in identifier:
            try:
                user = User.objects.get(email=identifier)
                identifier = user.username
            except User.DoesNotExist:
                raise serializers.ValidationError('Invalid email or password.')

        user = authenticate(username=identifier, password=password)

        if not user:
            raise serializers.ValidationError('Invalid credentials. Please check your username or email and password.')

        refresh = RefreshToken.for_user(user)
        access = refresh.access_token

        access['fullname'] = user.fullname
        access['username'] = user.username
        access['email'] = user.email
        access['role'] = getattr(user, 'role', 'Member')

        return {
            'access': str(access),
            'refresh': str(refresh)
        }