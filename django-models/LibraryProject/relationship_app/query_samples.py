"""
query_samples.py

Contains sample ORM queries demonstrating:
1) Query all books by a specific author.
2) List all books in a library.
3) Retrieve the librarian for a library.
"""

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian  # noqa: E402


def query_books_by_author(author_name: str):
    """
    Query all books by a specific author.
    """
    return Book.objects.filter(author__name=author_name)


def list_books_in_library(library_name: str):
    """
    List all books in a library.
    """
    return Book.objects.filter(libraries__name=library_name)


def get_librarian_for_library(library_name: str):
    """
    Retrieve the librarian for a library.
    """
    return Librarian.objects.get(library__name=library_name)


if __name__ == "__main__":
    # Optional demo output (safe: will just show empty QuerySets if no data exists)
    author_to_search = "George Orwell"
    library_to_search = "Central Library"

    print("Books by author:", author_to_search)
    print(list(query_books_by_author(author_to_search)))

    print("\nBooks in library:", library_to_search)
    print(list(list_books_in_library(library_to_search)))

    print("\nLibrarian for library:", library_to_search)
    try:
        print(get_librarian_for_library(library_to_search))
    except Librarian.DoesNotExist:
        print("No librarian found for that library (yet).")
