from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from utils.mixins import MultipleSerializerMixin

from .serializers import UserSerializer, UserListSerializer
from .models import CustomUser


class UserListCreateView(MultipleSerializerMixin, ListCreateAPIView):
    """ View to list and create users """
    queryset = CustomUser.objects.filter(is_staff=False)
    serializer_class = UserSerializer
    serializer_list = UserListSerializer

    # Excluir de la autenticación solo en la creación
    permissions = [AllowAny]  # Permite acceso sin autenticación solo al método POST
        


class UserRetrieveUpdateDestroyView(MultipleSerializerMixin, RetrieveUpdateDestroyAPIView):
    """ View to retrieve, update and delete an user """
    queryset = CustomUser.objects.filter(is_active=True, is_staff=False)
    serializer_class = UserSerializer
    serializer_list = UserListSerializer
    lookup_field = 'id'


    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete()
        return Response({'message': 'Usuario eliminado correctamente'}, status=status.HTTP_200_OK)

