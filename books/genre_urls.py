# books/urls.py
from django.urls import path
from .views import GenresView

urlpatterns = [
    path('', GenresView.as_view(), name='genres-list'),
]
