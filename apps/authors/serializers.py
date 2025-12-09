from rest_framework import serializers
from .models import Author
# Other app serializers
from apps.books.serializers import BooksForAuthorSerializer

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
    

class AuthorBooksListSerializer(serializers.ModelSerializer):
    """ Serializer to list all the books of an Author """
    # Traer todos los libros del autor (Relación inversa)
    books = BooksForAuthorSerializer(many=True, read_only=True)#Se tiene que llamar igual que el related_name del modelo de books
    #TRAE TODOS LOS CAMPOS DECLARADOS DEL BookSerializer

    class Meta:
        model = Author
        fields = ('id', 'name','lastname','age','books')
    

