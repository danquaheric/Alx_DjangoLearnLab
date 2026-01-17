import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def query_books_by_author(author_name):
    # Query all books by a specific author
    return Book.objects.filter(author__name=author_name)


def list_books_in_library(library_name):
    # List all books in a library
    library = Library.objects.get(name=library_name)
    return library.books.all()


def get_librarian_for_library(library_name):
    # Retrieve the librarian for a library
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)


if __name__ == "__main__":
    author_name = "George Orwell"
    library_name = "Central Library"

    print(query_books_by_author(author_name))
    print(list_books_in_library(library_name))
    try:
        print(get_librarian_for_library(library_name))
    except Librarian.DoesNotExist:
        print("No librarian found")
