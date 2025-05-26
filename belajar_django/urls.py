from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/v1/', include('users.urls')),
    path('api/v1/books/', include('books.urls')),
    path('api/v1/genres/', include('books.genre_urls')),
    path('api/v1/borrow/', include('borrow_records.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
