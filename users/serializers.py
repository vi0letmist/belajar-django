from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

# User Registration Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['fullname', 'username', 'password', 'email']

    def validate_email(self, value):
        # Check if the email is already taken
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already in use.")
        return value

    def validate_password(self, value):
        # Ensure password meets certain complexity requirements
        if len(value) < 6:
            raise serializers.ValidationError("Password must be at least 6 characters long.")
        return value

    def create(self, validated_data):
        # Hash the password before saving the user
        user = User.objects.create_user(**validated_data)
        return user

# JWT Token Serializer (For Login)
class TokenObtainPairSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        from django.contrib.auth import authenticate
        user = authenticate(**data)
        
        if not user:
            raise serializers.ValidationError('Invalid credentials. Please check your username and password.')
        
        refresh = RefreshToken.for_user(user)
        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }