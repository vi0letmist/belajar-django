# Create your models here.
from django.db import models
from django.utils.timezone import now
import uuid

class BookManager(models.Manager):
    pass

class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "genres"

    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    author = models.CharField(max_length=150, null=False, blank=False)
    isbn = models.CharField(unique=True)
    published_date = models.DateTimeField(null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    available_copies = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    objects = BookManager()

    class Meta:
        db_table = "books"

    def __str__(self):
        return f"{self.title} by {self.author} ({self.genre})"