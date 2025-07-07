from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from .serializers import RegisterSerializer, TokenObtainPairSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
                return Response({
                    "code": 201,
                    "message": "User registered successfully",
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({
                    "code": 500,
                    "message": f"Server error during user registration: {str(e)}",
                    "data": None
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            "code": 400,
            "message": "Validation error",
            "data": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = TokenObtainPairSerializer(data=request.data)
        
        if serializer.is_valid():
            return Response({
                "code": 200,
                "message": "Login successful",
                "data": serializer.validated_data
            }, status=status.HTTP_200_OK)

        return Response({
            "code": 400,
            "message": "Invalid credentials. Please check your username and password.",
            "data": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
