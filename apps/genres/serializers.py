from rest_framework import serializers
from .models import Genre

class GenreSerializer(serializers.ModelSerializer):
    """ Serializer to genres """
    class Meta:
        model = Genre
        fields = ('name',)
    

class GenreListSerializer(serializers.ModelSerializer):
    """ Serializer to list genres """
    class Meta:
        model = Genre
        fields = ('id', 'name')