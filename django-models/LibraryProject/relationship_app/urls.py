from django.contrib import admin
from django.urls import path, include
from .views import list_books, LibraryDetailView

urlpatterns = [
     path("admin/", admin.site.urls),
    path("", include("relationship_app.urls")),
    path("books/", list_books, name="list_books"),
    path("libraries/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
]
