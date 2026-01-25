from django import forms
from .models import Book

# Form for creating/editing books
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']  # adjust fields based on your Book model

# Tracker-specific example form
class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']  # can reuse same fields as BookForm
