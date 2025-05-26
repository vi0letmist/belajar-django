# books/serializers.py
from rest_framework import serializers
from .models import Book, Genre

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'cover', 'title', 'author', 'isbn', 'published_date',
                  'publisher', 'pages', 'description', 'language', 'genres',
                  'available_copies', 'created_at', 'updated_at', 'deleted_at']

class BookSerializerDetail(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all()
    )
    class Meta:
        model = Book
        fields = ['id', 'cover', 'title', 'author', 'isbn', 'published_date',
                  'publisher', 'pages', 'description', 'language',
                  'available_copies', 'genres']
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['genres'] = [genre.name for genre in instance.genres.all()]
        return rep

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']