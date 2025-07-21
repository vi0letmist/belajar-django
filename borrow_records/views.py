from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthenticated as CustomIsAuthenticated
from .models import BorrowRecords
from books.models import Book
from .serializers import BorrowRecordsSerializer, BorrowRecordsSerializerDetail, BorrowRecordsUpdateSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import OuterRef, Subquery, F
from django.utils.timezone import now

class BorrowRecordsListCreateView(APIView):
    """
    View to list all borrow records and create a new borrow records.
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
            
            queryset = BorrowRecords.objects.select_related('book', 'user').filter(deleted_at__isnull=True)

            if title:
                queryset = queryset.filter(book__title__icontains=title)

            queryset = queryset.order_by('created_at')

            total_records = queryset.count()
            last_page = (total_records + per_page - 1) // per_page if total_records > 0 else 0

            start = (page - 1) * per_page
            end = start + per_page
            paginated_queryset = queryset[start:end]

            serializer = BorrowRecordsSerializerDetail(paginated_queryset, many=True)
            return Response({
                "code": 200,
                "message": "Borrow Records retrieved successfully.",
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
        serializer = BorrowRecordsSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()

            response_data = {
                "id": data.id,
                "title": data.book.title if data.book else None,
                "author": data.book.author if data.book else None,
                "user_name": data.user.fullname if data.user else None,
                "borrow_date": data.borrow_date,
                "due_date": data.due_date,
                "return_date": data.return_date,
            }

            return Response({
                "code": 201,
                "message": "Borrow Records created successfully.",
                "data": response_data
            }, status=status.HTTP_201_CREATED)

        return Response({
            "code": 400,
            "message": "Invalid data provided.",
            "data": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class BorrowRecordsDetailView(APIView):
    """
    View to retrieve, update or delete a book instance.
    """
    permission_classes = [CustomIsAuthenticated]

    def get_object(self, pk):
        try:
            return BorrowRecords.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            borrow_record = self.get_object(pk)

            if borrow_record.deleted_at is not None:
                return Response({
                    "code": 404,
                    "message": "Borrow Records not found or has been deleted.",
                    "data": None
                }, status=status.HTTP_404_NOT_FOUND)

            serializer = BorrowRecordsSerializerDetail(borrow_record)
            return Response({
                "code": 200,
                "message": "Borrow Records retrieved successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except Http404:
            return Response({
                "code": 404,
                "message": "Borrow Records not found.",
                "data": None
            }, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({
                "code": 500,
                "message": f"An error occurred: {str(e)}",
                "data": None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        borrow_record = self.get_object(pk)
        serializer = BorrowRecordsUpdateSerializer(borrow_record, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "code": 200,
                "message": "Borrow Records updated successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            "code": 400,
            "message": "Invalid data provided.",
            "data": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            borrow_record = self.get_object(pk)

            borrow_record.deleted_at = now()
            borrow_record.save()

            response_data = {
                "id": borrow_record.id,
                "title": borrow_record.book.title if borrow_record.book else None,
                "author": borrow_record.book.author if borrow_record.book else None,
                "user_name": borrow_record.user.fullname if borrow_record.user else None,
                "borrow_date": borrow_record.borrow_date,
                "due_date": borrow_record.due_date,
                "return_date": borrow_record.return_date,
                "deleted_at": borrow_record.deleted_at
            }

            return Response({
                "code": 200,
                "message": "Borrow Records deleted successfully.",
                "data": response_data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "code": 500,
                "message": f"An error occurred: {str(e)}",
                "data": None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LastBorrowedBookView(APIView):
    """
    last borrowed book.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = request.user

            borrow_records = BorrowRecords.objects.select_related('book').prefetch_related('book__genres').filter(
                user=user,
                book__deleted_at__isnull=True
            ).order_by('book','-borrow_date').distinct('book')[:5]

            serializer = BorrowRecordsSerializerDetail(borrow_records, many=True)
            return Response({
                "code": 200,
                "message": "Book Records retrieved successfully.",
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