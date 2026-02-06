from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Book
from .serializers import BookSerializer

# -----------------------------------------
# List View – Read-only (public)
# -----------------------------------------
class BookListView(generics.ListAPIView):
    """
    Returns a list of all books.
    Accessible to unauthenticated users (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


# -----------------------------------------
# Detail View – Read-only (public)
# -----------------------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    Returns details of a single book by ID.
    Accessible to unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


# -----------------------------------------
# Create View – Authenticated only
# -----------------------------------------
class BookCreateView(generics.CreateAPIView):
    """
    Allows authenticated users to create a new book.
    Uses serializer validation (publication_year check).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# -----------------------------------------
# Update View – Authenticated only
# -----------------------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    Allows authenticated users to update an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# -----------------------------------------
# Delete View – Authenticated only
# -----------------------------------------
class BookDeleteView(generics.DestroyAPIView):
    """
    Allows authenticated users to delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
