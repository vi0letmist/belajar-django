from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.timezone import now
import uuid  # For generating UUIDs

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, role='Member', **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        if not username:
            raise ValueError("The Username field must be set")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('role', 'Admin')

        if extra_fields.get('role') != 'Admin':
            raise ValueError("Superuser must have the role 'Admin'.")

        return self.create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser):
    ROLE_CHOICES = [
        ('Member', 'Member'),
        ('Librarian', 'Librarian'),
        ('Admin', 'Admin'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fullname = models.CharField(max_length=255, null=False, blank=False)
    username = models.CharField(max_length=150, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    last_login = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'fullname']

    class Meta:
        db_table = "users"
        managed = True

    def __str__(self):
        return f"{self.username} ({self.role})"