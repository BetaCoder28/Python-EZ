# Middleware que extrae el access_token de las cookies y 
# lo coloca en el header Authorization
class JWTCookieMiddleware:
    # constructor estándar de middleware
    def __init__(self, get_response):
        self.get_response = get_response

    # Se ejecuta en cada request
    def __call__(self, request):
        access_token = request.COOKIES.get('access_token')

        # Si existe cookie access_token y NO hay header Authorization
        #Añade el header Authorization: Bearer {{token}}
        # Permite a DRF JWT Authentication funcionar automáticamente
        if access_token and not request.META.get('HTTP_AUTHORIZATION'):
            request.META['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'


        response = self.get_response(request)
        return response

