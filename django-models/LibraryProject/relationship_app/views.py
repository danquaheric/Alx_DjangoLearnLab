from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from .models import Book, Library


def list_books(request):
    """
    Function-based view:
    Lists all books stored in the database (title and author).
    """
    books = Book.objects.select_related("author").all()

    # If you are using templates (recommended), render HTML:
    return render(request, "relationship_app/list_books.html", {"books": books})

    # If you prefer plain text instead of HTML, use this:
    # lines = [f"{book.title} by {book.author.name}" for book in books]
    # return HttpResponse("\n".join(lines), content_type="text/plain")


class LibraryDetailView(DetailView):
    """
    Class-based view:
    Displays details for a specific library, listing all books in that library.
    """
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
