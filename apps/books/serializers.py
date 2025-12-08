from rest_framework import serializers
from datetime import date
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """ Serializer to books """
    class Meta:
        model = Book
        fields = ('id', 'title','description', 'year','author','genre','quantity')

    def validate_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError('El año no puede ser mayor al año actual')
        return value


class BookListSerializer(serializers.ModelSerializer):
    """ Serializer to list books """
    author = serializers.SerializerMethodField()
    # serializermethodfield
    # permite agregar campos personalizados calculados al serializador
    genre = serializers.SerializerMethodField()
    # Es un campo de solo lectura que te permite:
    # Agregar datos que no existen en el modelo
    # Realizar cálculos basados en otros campos
    # Formatear o transformar datos existentes
    # Acceder a relaciones complejas

    """"
        Para SerializerMethodField:
        1. Se debe declarar el campo 
        2. definir método que calcula valor
        método por defecto será:
        get_nombreCampo(self,obj)        
    """

    def get_author(self, obj):
        #obj es la instancia del modelo que se está serializando
        return {
            'id': obj.author.id,
            'name': obj.author.name,
            'lastname' : obj.author.lastname,
        }
    
    def get_genre(self,obj):
        return {
            'id': obj.genre.id,
            'name': obj.genre.name
        }

    class Meta:
        model = Book
        fields = ('id','title','description','year','author', 'genre', 'quantity')

    
class BooksForAuthorSerializer(serializers.ModelSerializer):
    """ Serializer to list books for author """
    genre = serializers.SerializerMethodField()

    def get_genre(self, obj):
        return {
            'id': obj.genre.id,
            'name': obj.genre.name
        }


    class Meta:
        model = Book
        # Coloca todos los campos menos los que se excluyen
        # Acción inversa a fields
        exclude = ('author','created_at','updated_at','is_active')