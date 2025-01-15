# books/serializers.py
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'published_date', 'genre', 'available_copies', 'created_at', 'updated_at', 'deleted_at']

class BookSerializerDetail(serializers.ModelSerializer):
    genre_name = serializers.CharField(source='genre.name', read_only=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'published_date', 'available_copies', 'genre_name']
