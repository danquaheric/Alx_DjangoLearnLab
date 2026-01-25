from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book


# -----------------------------
# List / View Books
# -----------------------------
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


# Alias view (optional but safe if referenced elsewhere)
@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/view_books.html', {'books': books})


# -----------------------------
# Create Book
# -----------------------------
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        Book.objects.create(title=title, author=author)
    return render(request, 'bookshelf/create_book.html')


# -----------------------------
# Edit Book
# -----------------------------
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.save()
    return render(request, 'bookshelf/edit_book.html', {'book': book})


# -----------------------------
# Delete Book
# -----------------------------
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        book.delete()
    return render(request, 'bookshelf/delete_book.html', {'book': book})
