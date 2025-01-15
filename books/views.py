from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthenticated as CustomIsAuthenticated
from .models import Book
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F

class BookListCreateView(APIView):
    """
    View to list all books and create a new book.
    """
    permission_classes = [CustomIsAuthenticated]

    def get(self, request):
        try:
            page = int(request.query_params.get('page', 1))
            per_page = int(request.query_params.get('limit', 10))
            title = request.query_params.get('title', None)

            if page < 1 or per_page < 1:
                return Response({
                    "code": 400,
                    "message": "'page' and 'limit' must be greater than 0.",
                    "data": None
                }, status=status.HTTP_400_BAD_REQUEST)

            filters = {}
            if title:
                filters['title__icontains'] = title

            total_records = Book.objects.filter(**filters).count()

            start = (page - 1) * per_page
            end = start + per_page
            last_page = (total_records + per_page - 1) // per_page if total_records > 0 else 0

            books = Book.objects.select_related('genre').filter(**filters).values(
                'id',
                'title',
                'author',
                'isbn',
                'published_date',
                'available_copies',
                genre_name=F('genre__name')
            ).order_by('created_at')[start:end]

            return Response({
                "code": 200,
                "message": "Books retrieved successfully.",
                "data": {
                    "page": page,
                    "total": total_records,
                    "per_page": per_page,
                    "last_page": last_page,
                    "data": list(books)
                }
            }, status=status.HTTP_200_OK)

        except ValueError:
            return Response({
                "code": 400,
                "message": "Invalid 'page' or 'limit' parameter. They must be integers.",
                "data": None
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "code": 500,
                "message": f"An error occurred: {str(e)}",
                "data": None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
