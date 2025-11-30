from django.db import models
from apps.core.models import BaseModel


class Book(BaseModel):
    title = models.CharField(
        max_length=100,
        verbose_name='Titulo'
    )
    description = models.TextField(
        verbose_name='Descripcion'
    )
    year = models.IntegerField(
        verbose_name='Año de publicacion'
    )
    author = models.ForeignKey(
        'authors.Author',
        on_delete=models.CASCADE, #si se elimina la clave el autor, se eliminan los libros
        verbose_name='Autor'
    )
    genre = models.ForeignKey(
        'genres.Genre',
        on_delete=models.CASCADE,
        verbose_name='Genero'
    )
    quantity = models.IntegerField(
        verbose_name='Cantidad de libros'
    )

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['year']

