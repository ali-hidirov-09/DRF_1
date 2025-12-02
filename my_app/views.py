from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Userlarga bog'liq CRUD ni qila oladi"""
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer

    # permission_classes = [permissions.IsAuthenticated] # Faqat ro'yxatdan o'tganlargina ko'ra oladi

