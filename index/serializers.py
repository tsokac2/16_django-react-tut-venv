from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Book, BookNumber, Character

class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model= BookNumber
        fields = ['id', 'isbn_10', 'isbn_13']


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):
    number = BookNumberSerializer(many=False)
    characters = CharacterSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id','title', 'description', 'number', 'characters']