from django.db import models
import uuid

class BookManager(models.Manager):
    pass

class TimestampWithoutTZField(models.DateTimeField):
    def db_type(self, connection):
        return 'timestamp without time zone'
    
class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    objects = models.Manager() 

    class Meta:
        db_table = "genres"

    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    LANGUAGE_CHOICES = [
        ("id", "Indonesian"),
        ("en", "English"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cover = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    title = models.CharField(max_length=255, null=False, blank=False)
    author = models.CharField(max_length=150, null=False, blank=False)
    isbn = models.CharField(unique=True)
    published_date = TimestampWithoutTZField(null=True, blank=True)
    publisher = models.CharField(max_length=150, null=True, blank=True)
    pages = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='id')
    genres = models.ManyToManyField(Genre, related_name="books")
    available_copies = models.IntegerField(default=0)
    created_at = TimestampWithoutTZField(auto_now_add=True)
    updated_at = TimestampWithoutTZField(auto_now=True)
    deleted_at = TimestampWithoutTZField(null=True, blank=True)
    objects = BookManager()

    class Meta:
        db_table = "books"

    def __str__(self):
        genres_list = ", ".join([genre.name for genre in self.genres.all()])  # pylint: disable=no-member
        return f"{self.title} by {self.author} [{genres_list}]"