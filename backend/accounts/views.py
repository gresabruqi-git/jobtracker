from rest_framework import generics, permissions
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
)

from .serializers import UserSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = []


class LoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []


class RefreshView(TokenRefreshView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []


class LogoutView(TokenBlacklistView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
