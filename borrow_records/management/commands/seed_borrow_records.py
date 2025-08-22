from django.core.management.base import BaseCommand
from borrow_records.models import BorrowRecords
from users.models import User
from books.models import Book
import uuid
from datetime import datetime


class Command(BaseCommand):
    help = "Seed borrow records data"

    def handle(self, *args, **kwargs):
        data = [
            {
                "id": "286f6749-9f9f-4bea-b0b0-da37feae27c0",
                "borrow_date": "2025-01-15 23:08:55.432",
                "due_date": "2025-01-30 15:00:00.000",
                "return_date": None,
                "created_at": "2025-01-15 23:08:55.432",
                "updated_at": "2025-01-15 23:08:55.432",
                "deleted_at": None,
                "book_id": "87561f47-4212-4e5c-a80d-584d937f6d76",
                "user_id": "432336d0-51f7-4ac8-9675-8f7e5063ae43",
            },
            {
                "id": "73fe36a0-b3ae-4f83-804b-b5d7fe83c977",
                "borrow_date": "2025-01-15 23:07:18.471",
                "due_date": "2025-01-30 20:00:00.000",
                "return_date": "2025-01-20 18:45:56.403",
                "created_at": "2025-01-15 23:07:18.471",
                "updated_at": "2025-01-20 18:45:56.403",
                "deleted_at": None,
                "book_id": "ee424991-1e86-4ee5-9133-8e3d19e2d40d",
                "user_id": "432336d0-51f7-4ac8-9675-8f7e5063ae43",
            },
            {
                "id": "f11bd440-77d4-4607-9a81-41f513209fce",
                "borrow_date": "2025-07-22 12:13:56.921",
                "due_date": "2025-07-30 15:00:00.000",
                "return_date": None,
                "created_at": "2025-07-22 12:13:56.921",
                "updated_at": "2025-07-22 12:13:56.921",
                "deleted_at": None,
                "book_id": "42bb7a27-b2c0-4202-bbd8-5e4b2cdf6199",
                "user_id": "432336d0-51f7-4ac8-9675-8f7e5063ae43",
            },
            {
                "id": "adb08bea-601c-4339-96b1-f7e8f223da44",
                "borrow_date": "2025-07-22 12:14:25.580",
                "due_date": "2025-08-30 15:00:00.000",
                "return_date": None,
                "created_at": "2025-07-22 12:14:25.580",
                "updated_at": "2025-07-22 12:14:25.580",
                "deleted_at": None,
                "book_id": "454beee4-a3eb-41f7-be6e-dbf8be3708e2",
                "user_id": "432336d0-51f7-4ac8-9675-8f7e5063ae43",
            },
            {
                "id": "673d4986-2636-44e2-ba36-7f7985e4afad",
                "borrow_date": "2025-07-22 12:15:05.072",
                "due_date": "2025-09-02 15:00:00.000",
                "return_date": None,
                "created_at": "2025-07-22 12:15:05.072",
                "updated_at": "2025-07-22 12:15:05.072",
                "deleted_at": None,
                "book_id": "ce951bd3-1e9a-4aa3-92fa-03039d206315",
                "user_id": "432336d0-51f7-4ac8-9675-8f7e5063ae43",
            },
        ]

        for record in data:
            user = User.objects.filter(id=record["user_id"]).first()
            book = Book.objects.filter(id=record["book_id"]).first()

            if not user or not book:
                self.stdout.write(self.style.WARNING(f"Skipping record {record['id']} - User/Book not found")) # pylint: disable=no-member
                continue

            BorrowRecords.objects.update_or_create(
                id=uuid.UUID(record["id"]),
                defaults={
                    "user": user,
                    "book": book,
                    "borrow_date": datetime.fromisoformat(record["borrow_date"]),
                    "due_date": datetime.fromisoformat(record["due_date"]) if record["due_date"] else None,
                    "return_date": datetime.fromisoformat(record["return_date"]) if record["return_date"] else None,
                    "created_at": datetime.fromisoformat(record["created_at"]),
                    "updated_at": datetime.fromisoformat(record["updated_at"]),
                    "deleted_at": datetime.fromisoformat(record["deleted_at"]) if record["deleted_at"] else None,
                }
            )

        self.stdout.write(self.style.SUCCESS("Borrow records seeded successfully")) # pylint: disable=no-member
