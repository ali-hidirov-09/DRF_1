from django.contrib.auth.models import User
from .models import Book
from rest_framework import viewsets
from .serializers import UserSerializer, BookSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Userlarga bog'liq CRUD ni qila oladi"""
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer

    # permission_classes = [permissions.IsAuthenticated] # Faqat ro'yxatdan o'tganlargina ko'ra oladi

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
