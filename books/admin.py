from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'isbn', 'published_date', 'genre', 'available_copies')
    list_filter = ('published_date', 'genre')
    search_fields = ('title', 'author', 'isbn')