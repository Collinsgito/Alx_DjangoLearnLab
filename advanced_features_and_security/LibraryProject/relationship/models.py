# relationship/models.py
from django.db import models
from django.conf import settings

class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return f"{self.name} ({self.location})"

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='books', null=True, blank=True)

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return self.title

class Librarian(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.username} - Librarian of {self.library.name}"

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Post by {self.author.username} at {self.created_at}"
