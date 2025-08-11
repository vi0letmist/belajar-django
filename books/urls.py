# books/urls.py
from django.urls import path
from .views import BookListCreateView, BookDetailView, BookNewCollectionsView, BookMustReadView

urlpatterns = [
    path('', BookListCreateView.as_view(), name='book-list-create'),
    path('<uuid:pk>', BookDetailView.as_view(), name='book-detail'),
    path('new-collections', BookNewCollectionsView.as_view(), name='book-new-collections'),
    path('must-read', BookMustReadView.as_view(), name='book-must-read'),
]
