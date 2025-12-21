from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings
from rest_framework import exceptions


class JWTCookieAuthentication(JWTAuthentication):
    def authenitcate(self, request):
        #Obtener el token de la cookie
        access_token = request.COOKIES.get('access_token')

        if access_token:
            request.META['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'

        # Lógica del padre
        return super().authenticate(request)
