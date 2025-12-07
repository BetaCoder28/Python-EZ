from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView,ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import Author
from .serializers import AuthorListSerializer, AuthorSerializer, BooksByAuthorListSerializer
from utils.mixins import MultipleSerializerMixin

# Heredar MultipleSerializerMixin para serializers diferentes 
class AuthorListCreateView(MultipleSerializerMixin, ListCreateAPIView):
    """ View to list and create authors """
    queryset = Author.objects.filter(is_active=True)
    serializer_class = AuthorSerializer #Para post
    serializer_list = AuthorListSerializer #Para get

# RetrieveUpdateDestroyAPIView -> Detalle actualizar eliminar
class AuthorRetrieveUpdateDestroyView(MultipleSerializerMixin,RetrieveUpdateDestroyAPIView):
    """ View to retrieve, update and delete an author """
    queryset = Author.objects.filter(is_active=True)
    serializer_class = AuthorSerializer
    serializers_list = AuthorListSerializer
    lookup_field = 'id'

    # *args, **kwargs -> recoge argumentos posicionales 
    # y keywords args que pasan desde la url asi no depende del nombre del parametro(pk, id, slug, etc)
    def delete(self, request, *args, **kwargs): #En vez de eliminar, marca is_active = False
        instance = self.get_object() #get_object método proveido? por las vistas genericas para obtener el objeto actual
        instance.soft_delete()
        return Response({'message' : 'Autor eliminado correctamente'}, status=status.HTTP_200_OK)


class BooksByAuthorListView(ListAPIView):
    """ View to list all the books of an author """
    queryset = Author.objects.prefetch_related('books').all()
    serializer_class = BooksByAuthorListSerializer