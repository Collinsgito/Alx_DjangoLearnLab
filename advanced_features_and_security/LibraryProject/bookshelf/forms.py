# LibraryProject/bookshelf/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Book

# --- existing CustomUser forms (if present) ---
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "date_of_birth", "profile_photo")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "date_of_birth", "profile_photo", "is_active", "is_staff")

# --- Book form ---
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "description"]
