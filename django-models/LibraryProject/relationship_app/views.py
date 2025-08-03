
from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView

def list_books(request):
    books = Book.objects.all()  # <- REQUIRED exactly like this
    return render(request, 'relationship_app/list_books.html', {'books': books})  # <- Match path exactly

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

    def get_queryset(self):
        return Library.objects.prefetch_related('books__author')
