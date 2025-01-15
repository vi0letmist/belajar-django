from django.urls import path
from .views import BorrowRecordsListCreateView, BorrowRecordsDetailView

urlpatterns = [
    path('', BorrowRecordsListCreateView.as_view(), name='borrow-records-list-create'),
    path('<uuid:pk>', BorrowRecordsDetailView.as_view(), name='borrow-records-detail'),
]
