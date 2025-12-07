from rest_framework import serializers
from datetime import date
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title','description', 'year','author','genre','quantity')

    def validate_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError('El año no puede ser mayor al año actual')
        return value


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

