class MultipleSerializerMixin:
    """ Mixin to allow using different serializers for listing and creating data """
    serializer_class = None # -> Para crear/actualizar
    serializer_list = None # -> Para listar

    def get_serializer_class(self):
        """ Determine which serializer to use on request method """
        if self.request.method == 'GET' and self.serializer_list:
            return self.serializer_list
        return self.serializer_class
    
# Flexibilidad -> usa diferentes serializers para diferentes acciones
# serializer para listar puede ser diferente al de crear