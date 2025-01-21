from mongoengine import Document, StringField, ReferenceField, ListField, BooleanField, EmailField, connect
from django.db import models

# Підключення до MongoDB
connect(db="email_system", host="mongodb+srv://dbuser:2KocWCKPaVTi5vzI@cluster0.pmbcv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

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
    tags = models.CharField(max_length=255, blank=True, null=True)  # Теги через кому

    def __str__(self):
        return self.text[:50]

class Contact(Document):
    fullname = StringField(required=True)
    email = EmailField(required=True, unique=True)
    is_sent = BooleanField(default=False)