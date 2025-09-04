from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # ✅ Filtering, searching, ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Filtering by attributes
    filterset_fields = ['title', 'author', 'publication_year']

    # Searching (title + author)
    search_fields = ['title', 'author']

    # Ordering (title + publication_year)
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering
