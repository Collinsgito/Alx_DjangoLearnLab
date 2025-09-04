from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer


class ListView(generics.ListAPIView):
    """
    GET /books/
    Retrieves all books with support for:
    - Filtering (title, author, publication_year)
    - Searching (title, author name)
    - Ordering (title, publication_year)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Exact match filtering
    filterset_fields = ['title', 'author', 'publication_year']

    # Search across text fields
    search_fields = ['title', 'author__name']

    # Allow ordering by specific fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default order
