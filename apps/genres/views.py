from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import Genre
from .serializers import GenreSerializer, GenreListSerializer
from utils.mixins import MultipleSerializerMixin


class GenreListCreateView(MultipleSerializerMixin, ListCreateAPIView):
    queryset = Genre.objects.filter(is_active=True)
    serializer_class = GenreSerializer
    serializer_list = GenreListSerializer


class GenreRetrieveUpdateDestroyView(MultipleSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.filter(is_active=True)
    serializer_class = GenreSerializer
    serializer_list = GenreListSerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete()
        return Response({'message': 'GÃ©nero eliminado correctamente'}, status=status.HTTP_200_OK)
