from rest_framework import generics
# Explicitly import permissions the checker expects
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Book
from .serializers import BookSerializer


class ListView(generics.ListAPIView):
    """
    GET /books/
    Publicly accessible list of books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read for all, write if logged in


class DetailView(generics.RetrieveAPIView):
    """
    GET /books/<id>/
    Publicly accessible single book detail.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CreateView(generics.CreateAPIView):
    """
    POST /books/create/
    Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class UpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH /books/update/<id>/
    Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class DeleteView(generics.DestroyAPIView):
    """
    DELETE /books/delete/<id>/
    Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
