from django.db import models

class BaseModel(models.Model):
    """ Modelo Base abstracto que proporciona campos comunes para todos los modelos del sistema """

    created_at = models.DateTimeField(
        auto_now_add=True, # automáticamente establece la fecha/hora actual cuando se crea el objeto
        verbose_name='Fecha de creación'
    )
    updated_at  = models.DateTimeField(
        auto_now=True, #Actualiza automaticamente cada que se guarda
        verbose_name='Fecha de actualización'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Activo'
    )

    class Meta:
        abstract = True #no crea tabla en la bd, solo es para herencia
        ordering = ['-created_at'] #Orden por defecto -> descendente por fecha de creación

    def soft_delete(self):
        """ Eliminación lógica del registro (Marca el registro como inactivo en vez de eliminarlo)"""
        self.is_active = False
        self.save()

    def restore(self):
        """ Restaurar registro eliminado lógicamente """
        self.is_active = True
        self.save()