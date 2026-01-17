from django.db import models

# Create your models here.
class Author(models.model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Book(models.model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title
    
class library(models.model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="libraries")

    def __str__(self):
        return self.name
    
class librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(library, on_delete=models.CASCADE, related_name="librarian")

    def __str__(self):
        return self.name