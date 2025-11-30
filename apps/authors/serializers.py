from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer): #para crear/actualizar
    """ Serializer to Authors """
    class Meta:
        model = Author
        fields = ('name','lastname', 'age') #Campos editables


    def validate_age(self, value): #Validación personalizada
        if value < 18:
            raise serializers.ValidationError("El autor debe ser mayor de edad")
        if value > 100:
            raise serializers.ValidationError("Edad no valida")
        return value


class AuthorListSerializer(serializers.ModelSerializer): #Para listar
    """ Serializer to list authors """ #Convertir entre objetos python y JSON
    class Meta:
        model = Author
        fields = '__all__' #Todos los campos incluyendo IDs
    


    

