from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.core.models import BaseModel


class Author(BaseModel): #Hereda de basemodel (created_at, updated_at, is_active)
    """ Modelo que representa a un autor de libros """
    name = models.CharField(
        max_length= 100,
        verbose_name='Nombre'
    )
    lastname = models.CharField(
        max_length=100,
        verbose_name='Apellido'
    )
    age = models.IntegerField(
        validators=[
            MinValueValidator(18, message="El autor debe ser mayor de edad"),
            MaxValueValidator(100, message="Edad no valida")
        ],
        verbose_name='Edad'
    )


    def __str__(self):
        name = self.name
        return name
    
    class Meta:
        verbose_name = ('Autor')
        verbose_name_plural = ('Autores')