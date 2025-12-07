from django.urls import path

from apps.books.views import BookListCreateView, BookRetrieveUpdateDestroyView

urlpatterns = [
    path(
        "books/",
        BookListCreateView.as_view(),
        name="book",
    ),
    path(
        "books/<int:id>/",
        BookRetrieveUpdateDestroyView.as_view(),
        name="book-detail",
    ),
]