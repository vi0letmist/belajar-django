from django.contrib import admin
from .models import BorrowRecords

@admin.register(BorrowRecords)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'book_id', 'borrow_date', 'due_date', 'return_date')
    list_filter = ('borrow_date', 'due_date', 'return_date')
    search_fields = ('user_id', 'book')