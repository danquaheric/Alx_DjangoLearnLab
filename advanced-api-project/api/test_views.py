# api/test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test users
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.admin_user = User.objects.create_superuser(username='admin', password='adminpass')

        # Create test data
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book1 = Book.objects.create(title="Harry Potter 1", publication_year=1997, author=self.author)
        self.book2 = Book.objects.create(title="Harry Potter 2", publication_year=1998, author=self.author)

        # API endpoints
        self.list_url = reverse('book-list')  
        self.detail_url = lambda pk: reverse('book-detail', args=[pk])
        self.create_url = reverse('book-create')

    # -----------------------------
    # Example test using self.client.login
    # -----------------------------
    def test_create_book_with_client_login(self):
        # Login using Django's session authentication
        login_successful = self.client.login(username='testuser', password='password123')
        self.assertTrue(login_successful)

        data = {
            'title': "Harry Potter 3",
            'publication_year': 1999,
            'author': self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # You can still keep JWT-based tests separately if needed
