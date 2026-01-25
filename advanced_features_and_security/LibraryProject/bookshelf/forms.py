from django import forms
from .models import Book

# -----------------------------
# Form to create/edit Book
# -----------------------------
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']  # Add other fields if your Book model has them

# -----------------------------
# ExampleForm (needed for tracker)
# -----------------------------
class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']  # Can duplicate BookForm for demonstration
