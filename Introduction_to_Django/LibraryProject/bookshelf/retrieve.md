
# Retrieve the Book instance using Book.objects.get()

```python
from bookshelf.models import Book

# Retrieve the book with title "1984"
book = Book.objects.get(title="1984")

# Display book details
print(book.title)
print(book.author)
print(book.publication_year)
