# books/serializers.py
from rest_framework import serializers
from .models import BorrowRecords, Book

class BorrowRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecords
        fields = ['id', 'user', 'book', 'borrow_date', 'due_date', 'return_date', 'created_at', 'updated_at', 'deleted_at']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'published_date']

class BorrowRecordsSerializerDetail(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    user_name = serializers.CharField(source='user.fullname', read_only=True)

    class Meta:
        model = BorrowRecords
        fields = ['id', 'borrow_date', 'due_date', 'return_date', 'book', 'user_name']
        depth = 1


