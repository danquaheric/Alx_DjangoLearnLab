from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm, ExampleForm


# -----------------------------
# List / View Books
# -----------------------------
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # ORM prevents SQL injection
    return render(request, 'bookshelf/book_list.html', {'books': books})


# Optional alias view (safe if referenced elsewhere)
@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/view_books.html', {'books': books})


# -----------------------------
# Create Book (SECURE)
# -----------------------------
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'bookshelf/form_example.html', {'form': form})


# -----------------------------
# Edit Book (SECURE)
# -----------------------------
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
    return render(request, 'bookshelf/edit_book.html', {'form': form, 'book': book})


# -----------------------------
# Delete Book
# -----------------------------
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
    return render(request, 'bookshelf/delete_book.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    form = ExampleForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'bookshelf/form_example.html', {'form': form})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_example(request):
    form = ExampleForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'bookshelf/form_example.html', {'form': form})


