from django import forms
from .models import Book


# Existing form for Book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

# ExampleForm (needed for tracker)
class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']  # You can duplicate fields for demonstration