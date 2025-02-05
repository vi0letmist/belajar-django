# Generated by Django 5.1.4 on 2024-12-30 15:02

import django.db.models.deletion
import uuid
from django.db import migrations, models

def add_default_genres(apps, schema_editor):
    Genre = apps.get_model('books', 'Genre')
    default_genres = ['Fiction', 'Non-Fiction', 'Poetry', 'Graphic Novels/Comics', 'Mystery/Thriller'
                      , 'Romance', 'Science Fiction', 'Fantasy', 'Horror', 'History', 'Science'
                      , 'Biography/Autobiography', 'Self-Help', 'Health & Wellness', 'Business & Economics'
                      , 'Psychology', 'Politics', 'Religion & Spirituality', 'Art & Photography', 'Humor']
    for genre_name in default_genres:
        Genre.objects.create(name=genre_name)

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'genres',
            },
        ),
        migrations.RunPython(add_default_genres),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=150)),
                ('isbn', models.CharField(unique=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('available_copies', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.genre')),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]
