from index.serializers import BookSerializer
from django.shortcuts import render
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication


def first(request):
    books = Book.objects.all()
    return render(request,'base.html', {'books':books})


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)