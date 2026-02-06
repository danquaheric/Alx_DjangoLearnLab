from django.db import models

# -----------------------------
# Author Model
# -----------------------------
class Author(models.Model):
    """
    Represents an author.
    One author can have multiple books (one-to-many relationship).
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# -----------------------------
# Book Model
# -----------------------------
class Book(models.Model):
    """
    Represents a book written by an author.
    Each book is linked to a single author.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
