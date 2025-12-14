from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """ Serializer to Users(No superuser) """
    #Acepta en el request pero nunca lo devuelve en la respuesta
    password = serializers.CharField(write_only=True)

    class Meta:
        model =  CustomUser
        fields = ('first_name', 'last_name', 'email', 'password')
        extra_kwargs = { #Modificar cómo se comporta un campo del modelo solo en este serializer
            'email': {#Se modifica el campo email
                'validators': [ #Validación que el campo sea único
                    UniqueValidator(
                        queryset=CustomUser.objects.all(),
                        message='El correo ya está registrado'
                    )
                ]
            }
        }

    # Sobreescribir el método create para que el username sea el email
    def create(self, validated_data):
        validated_data['username'] = validated_data['email']
        return CustomUser.objects.create_user(**validated_data)



class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model =  CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')