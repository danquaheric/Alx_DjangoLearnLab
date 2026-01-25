from django import forms
from .models import Book


class ExampleForm(forms.ModelForm):
    """
    ExampleForm is used to demonstrate secure form handling,
    including validation and CSRF protection.
    """
    class Meta:
        model = Book
        fields = '__all__'


# Optional: keep BookForm if already used elsewhere
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
