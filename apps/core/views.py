from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

# Vista personalizada para el login que devuelve tokens en cookies HTTP-Only
class CookieTokenObtainPairView(TokenObtainPairView):
    # Maneja la solicitud POST de login
    def post(self, request, *args, **kwargs ):
        # Obtiene el serializador de TokenObtainPairSerializer
        serializer = self.get_serializer(data=request.data)
        try:
            # Valida credenciales
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        
        response = Response({"detail" : "Acceso exitoso"}, status=status.HTTP_200_OK)

        # Es el diccionario que contiene los tokens generados por el 
        # serializador después de una validación exitosa 
        # Este diccionario tiene dos claves principales: 
        # 'access' (token de acceso) y 'refresh' (token de refresco)
        tokens = serializer.validated_data
        
        response.set_cookie(
            key='access_token', #Nombre de la cookie para solicitudes
            value=str(tokens['access']), #Asignar el valor de la cookie -> el token de acceso obtenido del serializador(tokens)
            # Tiempo de vida
            max_age=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].total_seconds(),
            # True indica que no sea accesible por JavaScript
            httponly=True,
            # Si secure=True,cookie solo se enviará en solicitudes HTTPS
            secure=settings.SIMPLE_JWT.get('AUTH_COOKIE_SECURE',False),
            #SameSite->medida de seguridad para Cross-Site Request Forgery (CSRF) 
            #El atributo SameSite indica cómo se debe enviar la cookie en
            #solicitudes que provienen de diferentes orígenes o dominios
            #el navegador puede bloquear o permitir el envío de cookies
            
            #SameSite=Strict, la cookie solo se enviará en solicitudes que 
            #provengan del mismo origen o dominio (solo se enviará 
            #si la solicitud se hace directamente desde la misma página web
            #o dominio que emitió la cookie).

            #SameSite=Lax es un equilibrio entre seguridad y usabilidad 
            #Permite que las cookies se envíen en ciertos escenarios de navegación cruzada.
            
            #SameSite=None, las cookies se enviarán siempre
            samesite=settings.SIMPLE_JWT.get('AUTH_COOKIE_SAMESITE','Lax'),
            path='/' #Especifica la ruta para la que la ruta será valida
            # Con '/' será valida para todas las rutas del dominio
        )
        response.set_cookie(
            key='refresh_token',
            value=str(tokens['refresh']),
            max_age=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'].total_seconds(),
            httponly=True,
            secure=settings.SIMPLE_JWT.get('AUTH_COOKIE_SECURE',False),
            samesite=settings.SIMPLE_JWT.get('AUTH_COOKIE_SAMESITE','Lax'),
            path='/api/v1/auth/refresh/',#Solo se envía a esta ruta específica
        )
        return response
    
# Renueva el access_token usando el refresh_token
class CookieTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        # Extrae token de la cookie
        refresh_token = request.COOKIES.get('refresh_token')
        if not refresh_token:
            return Response(
                {"detail" : "Refresh token no encontrado"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        # obtiene y valida el refresh_token
        serializer = self.get_serializer(data={"refresh": refresh_token})
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            return Response(
                {"detail" : "Token inválido o expirado"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        response = Response({"detail" : "Token renovado"}, status=status.HTTP_200_OK)
        # Devuelve nuevo access_token en cookie
        response.set_cookie(
            key='access_token',
            value=str(serializer.validated_data['access']),
            max_age=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].total_seconds(),
            httponly=True,
            secure=settings.SIMPLE_JWT.get('AUTH_COOKIE_SECURE',False),
            samesite=settings.SIMPLE_JWT.get('AUTH_COOKIE_SAMESITE','Lax'),
            path = '/'
        )
        return response


class LogoutView(TokenRefreshView):
    # Elimina las cookies de autenticación
    def post(self, request, *args, **kwargs):
        response = Response({"detail" : "Sesión cerrada"}, status=status.HTTP_200_OK)
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        return response

