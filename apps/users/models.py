from django.db import models
from apps.core.models import BaseModel
from django.contrib.auth.models import AbstractUser
""" AbstractUser contain
    - username
    - first_name
    - last_name
    - email
    - password
    - is_staff #default False, no usar
    - is_active #default True
    - date_joined #default timezone.now
"""


class Role(BaseModel):
    """ Role of an user """
    role = models.CharField(
        max_length=100,
        verbose_name='Rol'
    )

    def __str__(self):
        return self.role
    
    class Meta:
        verbose_name = ('Rol')
        verbose_name_plural = ('Roles')
    

class CustomUser(AbstractUser):
    """ Custom User  """
    email = models.EmailField(
        unique=True,
        verbose_name='Correo electrónico'
    )
    roleId = models.ForeignKey(
        'users.Role',
        on_delete=models.PROTECT, #Evitar la eliminación de un rol si está en uso
        # COn models.SET_NULL, se puede establecer el valor en NULL si se elimina el rol
        null=True,
        verbose_name='Rol'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Fecha de actualización'
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = ('Usuario')
        verbose_name_plural = ('Usuarios')
        ordering = ['-date_joined']

    def soft_delete(self):
        self.is_active = False
        self.save()

    def restore(self):
        self.is_active = True
        self.save()