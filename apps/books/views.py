from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer, BookListSerializer
from utils.mixins import MultipleSerializerMixin


class BookListCreateView(MultipleSerializerMixin, ListCreateAPIView):
    """ View to list and create books """
    queryset = Book.objects.filter(is_active=True)
    serializer_class = BookSerializer
    serializer_list = BookListSerializer


class BookRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """ View to retrieve, update and delete a book """
    queryset = Book.objects.filter(is_active=True)
    serializer_class = BookSerializer
    serializer_list = BookListSerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete()
        return Response({'message' : 'Libro eliminado correctamente'}, status=status.HTTP_200_OK)
    
    