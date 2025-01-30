from rest_framework import serializers
from .models import BorrowRecords, Book
from django.utils.timezone import now

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

class BorrowRecordsUpdateSerializer(serializers.ModelSerializer):
    return_book = serializers.BooleanField(write_only=True, required=False)

    class Meta:
        model = BorrowRecords
        fields = ['due_date', 'return_book']

    def update(self, instance, validated_data):
        return_book = validated_data.pop('return_book', None)
        
        if return_book:
            instance.return_date = now()

        instance.due_date = validated_data.get('due_date', instance.due_date)

        instance.save()
        return instance
