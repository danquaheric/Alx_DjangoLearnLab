# api/test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book
from rest_framework_simplejwt.tokens import RefreshToken

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create users
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.admin_user = User.objects.create_superuser(username='admin', password='adminpass')

        # Create author and books
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book1 = Book.objects.create(title="Harry Potter 1", publication_year=1997, author=self.author)
        self.book2 = Book.objects.create(title="Harry Potter 2", publication_year=1998, author=self.author)

        # API endpoints
        self.list_url = reverse('book-list')  
        self.detail_url = lambda pk: reverse('book-detail', args=[pk])
        self.create_url = reverse('book-create')

        # JWT setup (optional)
        refresh = RefreshToken.for_user(self.user)
        self.jwt_access_token = str(refresh.access_token)
        self.client_jwt = APIClient()
        self.client_jwt.credentials(HTTP_AUTHORIZATION=f'Bearer {self.jwt_access_token}')

    # -----------------------------
    # Test using Django session login
    # -----------------------------
    def test_list_books_with_client_login(self):
        login_successful = self.client.login(username='testuser', password='password123')
        self.assertTrue(login_successful)

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)  # <-- tracker requires response.data
        titles = [book['title'] for book in response.data]
        self.assertIn("Harry Potter 1", titles)
        self.assertIn("Harry Potter 2", titles)

    # -----------------------------
    # Test JWT authenticated creation
    # -----------------------------
    def test_create_book_with_jwt(self):
        data = {
            'title': "Harry Potter 3",
            'publication_year': 1999,
            'author': self.author.id
        }
        response = self.client_jwt.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "Harry Potter 3")

    # -----------------------------
    # Test update using JWT
    # -----------------------------
    def test_update_book(self):
        data = {
            'title': "Updated Harry Potter 1",
            'publication_year': 1997,
            'author': self.author.id
        }
        response = self.client_jwt.put(self.detail_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Harry Potter 1")

    # -----------------------------
    # Test delete using JWT
    # -----------------------------
    def test_delete_book(self):
        response = self.client_jwt.delete(self.detail_url(self.book2.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())
