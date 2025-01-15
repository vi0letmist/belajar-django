from django.db import models
import uuid
from users.models import User
from books.models import Book

class BorrowRecordsManager(models.Manager):
    pass

class TimestampWithoutTZField(models.DateTimeField):
    def db_type(self, connection):
        return 'timestamp without time zone'

class BorrowRecords(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    borrow_date = TimestampWithoutTZField(auto_now_add=True)
    due_date = TimestampWithoutTZField(null=True, blank=True)
    return_date = TimestampWithoutTZField(null=True, blank=True)
    created_at = TimestampWithoutTZField(auto_now_add=True)
    updated_at = TimestampWithoutTZField(auto_now=True)
    deleted_at = TimestampWithoutTZField(null=True, blank=True)
    objects = BorrowRecordsManager()

    class Meta:
        db_table = "borrow_records"

    def __str__(self):
        return f"Borrow record {self.id}: {self.user} borrowed {self.book}"