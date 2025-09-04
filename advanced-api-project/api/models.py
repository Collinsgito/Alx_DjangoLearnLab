from django.db import models

class Author(models.Model):
    """
    Author model represents a book author.
    - name: stores the author's full name
    One Author can be linked to many Books (one-to-many relationship).
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents a written book.
    - title: the book's title
    - publication_year: the year it was published
    - author: ForeignKey linking the book to its author (many-to-one)
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author, related_name="books", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

