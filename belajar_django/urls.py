from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/v1/', include('users.urls')),
    path('api/v1/books/', include('books.urls')),
    path('api/v1/borrow/', include('borrow_records.urls')),
]
