from django.urls import path
from .views import BorrowRecordsListCreateView, BorrowRecordsDetailView, LastBorrowedBookView

urlpatterns = [
    path('', BorrowRecordsListCreateView.as_view(), name='borrow-records-list-create'),
    path('<uuid:pk>', BorrowRecordsDetailView.as_view(), name='borrow-records-detail'),
    path('last-borrowed', LastBorrowedBookView.as_view(), name='last-borrowed-book'),
]
