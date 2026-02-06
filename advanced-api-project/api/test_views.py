# api/test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Author, Book
from django.contrib.auth.models import User


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test users
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.admin_user = User.objects.create_superuser(username='admin', password='adminpass')

        # Obtain JWT tokens
        self.user_token = str(RefreshToken.for_user(self.user).access_token)
        self.admin_token = str(RefreshToken.for_user(self.admin_user).access_token)

        # Auth headers
        self.user_auth_header = {'HTTP_AUTHORIZATION': f'Bearer {self.user_token}'}
        self.admin_auth_header = {'HTTP_AUTHORIZATION': f'Bearer {self.admin_token}'}

        # Create test data
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book1 = Book.objects.create(title="Harry Potter 1", publication_year=1997, author=self.author)
        self.book2 = Book.objects.create(title="Harry Potter 2", publication_year=1998, author=self.author)

        # API endpoints
        self.list_url = reverse('book-list')  # Generic ListView endpoint
        self.detail_url = lambda pk: reverse('book-detail', args=[pk])
        self.create_url = reverse('book-create')
        self.update_url = lambda pk: reverse('book-update', args=[pk])
        self.delete_url = lambda pk: reverse('book-delete', args=[pk])

    # -----------------------------
    # Test GET /books/ (list)
    # -----------------------------
    def test_list_books_authenticated(self):
        response = self.client.get(self.list_url, **self.user_auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_books_unauthenticated(self):
        response = self.client.get(self.list_url)
        # Read-only allowed
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # -----------------------------
    # Test POST /books/create
    # -----------------------------
    def test_create_book_authenticated(self):
        data = {
            'title': "Harry Potter 3",
            'publication_year': 1999,
            'author': self.author.id
        }
        response = self.client.post(self.create_url, data, **self.user_auth_header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        data = {
            'title': "Harry Potter 4",
            'publication_year': 2000,
            'author': self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # -----------------------------
    # Test GET /books/<id>/ (detail)
    # -----------------------------
    def test_retrieve_book(self):
        response = self.client.get(self.detail_url(self.book1.id), **self.user_auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Harry Potter 1")

    # -----------------------------
    # Test PUT /books/<id>/update
    # -----------------------------
    def test_update_book(self):
        data = {'title': "Harry Potter 1 Updated", 'publication_year': 1997, 'author': self.author.id}
        response = self.client.put(self.update_url(self.book1.id), data, **self.admin_auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Harry Potter 1 Updated")

    # -----------------------------
    # Test DELETE /books/<id>/delete
    # -----------------------------
    def test_delete_book(self):
        response = self.client.delete(self.delete_url(self.book2.id), **self.admin_auth_header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # -----------------------------
    # Test filtering
    # -----------------------------
    def test_filter_books_by_title(self):
        response = self.client.get(f"{self.list_url}?title=Harry Potter 1", **self.user_auth_header)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Harry Potter 1")

    # -----------------------------
    # Test ordering
    # -----------------------------
    def test_order_books_by_publication_year_desc(self):
        response = self.client.get(f"{self.list_url}?ordering=-publication_year", **self.user_auth_header)
        self.assertEqual(response.data[0]['publication_year'], 1998)

    # -----------------------------
    # Test search
    # -----------------------------
    def test_search_books_by_author(self):
        response = self.client.get(f"{self.list_url}?search=Rowling", **self.user_auth_header)
        self.assertEqual(len(response.data), 2)
