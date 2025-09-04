# views.py

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # 🔹 Filtering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["title", "author", "publication_year"]

    # 🔹 Searching
    search_fields = ["title", "author"]

    # 🔹 Ordering
    ordering_fields = ["title", "publication_year"]
    ordering = ["title"]  # optional default
