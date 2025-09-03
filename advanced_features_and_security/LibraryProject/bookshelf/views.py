
# LibraryProject/bookshelf/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.core.exceptions import PermissionDenied
from .models import Book
from .forms import BookForm,ExampleForm

# List / view all books (requires can_view)
@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

# Create book (requires can_create)
@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.created_by = request.user
            book.save()
            return redirect("bookshelf:book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/book_form.html", {"form": form})

# Edit book (requires can_edit)
@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("bookshelf:book_list")
    return render(request, "bookshelf/book_form.html", {"form": form, "book": book})

# Delete book (requires can_delete)
@permission_required("bookshelf.can_delete", raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("bookshelf:book_list")
    return render(request, "bookshelf/book_confirm_delete.html", {"book": book})

# Detail view (also guarded by can_view)
@permission_required("bookshelf.can_view", raise_exception=True)
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "bookshelf/book_detail.html", {"book": book})
def example_form_view(request):
    """View demonstrating CSRF token and safe form handling."""
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Safe handling: cleaned_data prevents SQL injection
            name = form.cleaned_data["name"]
            message = form.cleaned_data["message"]
            # For demo, just pass data back to template
            return render(request, "bookshelf/form_example.html", {
                "form": form,
                "submitted": True,
                "name": name,
                "message": message,
            })
    else:
        form = ExampleForm()

    return render(request, "bookshelf/form_example.html", {"form": form})