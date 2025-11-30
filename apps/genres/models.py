from django.db import models
from apps.core.models import BaseModel

class Genre(BaseModel):
    """ Modelo que representa un genero de libros """
    name = models.CharField(
        max_length=50,
        verbose_name='Nombre'
    )

    def __str__(self):
        name = self.name
        return name
    
    class Meta:
        verbose_name = ('Genero')
        verbose_name_plural = ('Autores')

