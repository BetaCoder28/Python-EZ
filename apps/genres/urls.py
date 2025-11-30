from django.urls import path
from apps.genres.views import GenreListCreateView, GenreRetrieveUpdateDestroyView

urlpatterns = [
    path(
        'genres/',
        GenreListCreateView.as_view(), 
        name='genre'
    ),
    path(
        'genres/<int:id>/',
        GenreRetrieveUpdateDestroyView.as_view(),
        name='genre-detail'
    )
]