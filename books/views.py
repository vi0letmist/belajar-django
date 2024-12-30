from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthenticated as CustomIsAuthenticated
from .models import Book
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

class BookListCreateView(APIView):
    """
    View to list all books and create a new book.
    """
    permission_classes = [CustomIsAuthenticated]

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({
            "code": 200,
            "message": "Books retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "code": 201,
                "message": "Book created successfully.",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            "code": 400,
            "message": "Invalid data provided.",
            "data": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class BookDetailView(APIView):
    """
    View to retrieve, update or delete a book instance.
    """
    permission_classes = [CustomIsAuthenticated]

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response({
            "code": 200,
            "message": "Book retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "code": 200,
                "message": "Book updated successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            "code": 400,
            "message": "Invalid data provided.",
            "data": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response({
            "code": 204,
            "message": "Book deleted successfully.",
            "data": None
        }, status=status.HTTP_204_NO_CONTENT)
