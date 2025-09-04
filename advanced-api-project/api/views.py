from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


class ListView(generics.ListAPIView):
    """
    GET /books/
    Retrieves a list of all books.
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class DetailView(generics.RetrieveAPIView):
    """
    GET /books/<id>/
    Retrieves a single book by its ID.
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class CreateView(generics.CreateAPIView):
    """
    POST /books/create/
    Creates a new book.
    Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Extra hook to customize save behavior.
        For example, you could log the user who created the book.
        """
        serializer.save()


class UpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH /books/<id>/update/
    Updates an existing book.
    Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Custom behavior for updates.
        You can enforce extra rules or logging here.
        """
        serializer.save()


class DeleteView(generics.DestroyAPIView):
    """
    DELETE /books/<id>/delete/
    Deletes a book.
    Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
