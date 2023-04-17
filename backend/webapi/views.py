from django.shortcuts import render

# Create your views here.
 
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer