from django.urls import path

from apps.authors.views import (
    AuthorListCreateView, AuthorRetrieveUpdateDestroyView, BooksByAuthorListView
)

urlpatterns = [
    path(
        'author/',
        AuthorListCreateView.as_view(),
        name='author'
    ),#GET lista, POST crear
    path(
        'author/<int:id>/',
        AuthorRetrieveUpdateDestroyView.as_view(),
        name='author-detail'
    ), #GET/PUT/DELETE especifico -> http://localhost:8000/author/1580/
    path(
        'author/<int:id>/books/',
        BooksByAuthorListView.as_view(),
        name='author-books'
    ), 
]