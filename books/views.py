from .permissions import CustomIsAuthenticated
from .models import Book, Genre
from borrow_records.models import BorrowRecords
from .serializers import BookSerializer, BookSerializerDetail, GenreSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F
from django.utils.timezone import now

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

            queryset = Book.objects.prefetch_related('genres').filter(deleted_at__isnull=True)

            if title:
                queryset = queryset.filter(title__icontains=title)

            queryset = queryset.order_by('created_at')

            total_records = queryset.count()
            last_page = (total_records + per_page - 1) // per_page if total_records > 0 else 0

            start = (page - 1) * per_page
            end = start + per_page
            paginated_queryset = queryset[start:end]

            serializer = BookSerializerDetail(paginated_queryset, many=True)
            return Response({
                "code": 200,
                "message": "Book retrieved successfully.",
                "data": {
                    "page": page,
                    "total": total_records,
                    "per_page": per_page,
                    "last_page": last_page,
                    "data": serializer.data,
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
            book = serializer.save()
            genre_names = [genre.name for genre in book.genres.all()]

            response_data = {
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "genre_name": genre_names,
            }

            return Response({
                "code": 201,
                "message": "Book created successfully.",
                "data": response_data
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
        try:
            book = self.get_object(pk)

            if book.deleted_at is not None:
                return Response({
                    "code": 404,
                    "message": "Book not found or has been deleted.",
                    "data": None
                }, status=status.HTTP_404_NOT_FOUND)

            serializer = BookSerializerDetail(book)
            return Response({
                "code": 200,
                "message": "Book retrieved successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except Http404:
            return Response({
                "code": 404,
                "message": "Book not found.",
                "data": None
            }, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({
                "code": 500,
                "message": f"An error occurred: {str(e)}",
                "data": None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializerDetail(book, data=request.data)
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
        try:
            book = self.get_object(pk)

            book.deleted_at = now()
            book.save()

            response_data = {
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "genre_name": book.genre.name if book.genre else None,
                "deleted_at": book.deleted_at
            }

            return Response({
                "code": 200,
                "message": "Book deleted successfully.",
                "data": response_data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "code": 500,
                "message": f"An error occurred: {str(e)}",
                "data": None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class BookNewCollectionsView(APIView):
    """
    new collections book.
    """
    permission_classes = [CustomIsAuthenticated]

    def get(self, request):
        try:
            books = Book.objects.filter(deleted_at__isnull=True).order_by(F('created_at').desc()).distinct()[:5]

            serializer = BookSerializerDetail(books, many=True)
            return Response({
                "code": 200,
                "message": "Book retrieved successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except Http404:
            return Response({
                "code": 404,
                "message": "Book not found.",
                "data": None
            }, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({
                "code": 500,
                "message": f"An error occurred: {str(e)}",
                "data": None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BookMustReadView(APIView):
    """
    must read selection books.
    """
    permission_classes = [CustomIsAuthenticated]

    def get(self, request):
        try:
            books = Book.objects.filter(is_must_read=True, deleted_at__isnull=True)

            serializer = BookSerializerDetail(books, many=True)
            return Response({
                "code": 200,
                "message": "Book retrieved successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except Http404:
            return Response({
                "code": 404,
                "message": "Book not found.",
                "data": None
            }, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({
                "code": 500,
                "message": f"An error occurred: {str(e)}",
                "data": None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GenresView(APIView):
    """
    View to list all genres.
    """
    permission_classes = [CustomIsAuthenticated]

    def get(self, request):
        try:
            genres = Genre.objects.all()

            serializer = GenreSerializer(genres, many=True)
            return Response({
                "code": 200,
                "message": "Genres retrieved successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "code": 500,
                "message": f"An error occurred: {str(e)}",
                "data": None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)