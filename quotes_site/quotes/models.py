from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass

class Author(models.Model):
    fullname = models.CharField(max_length=255)
    born_date = models.CharField(max_length=255, blank=True, null=True)
    born_location = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.fullname

class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='quotes')
    tags = models.CharField(max_length=255, blank=True, null=True)  # Зберігаємо теги як строку через кому

    def __str__(self):
        return self.text[:50]