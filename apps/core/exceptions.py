from rest_framework.views import exception_handler
from rest_framework import status
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    """  Manejo personalizado de excepciones para toda la API """

    # Call drf default exception handler first
    response = exception_handler(exc, context)

    if response is not None:
        # Personalizar la respuesta del error
        error_payload = {
            'error' : {
                'code' : response.status_code,
                'message' : response.data.get('detail', 'Ha ocurrido un error'),
                'details' : response.data
            }
        }
        response.data = error_payload
    else:
        # Manejar excepciones no capturadas por drf
        logger.error(f"Excepción no manejada: {exc}", exc_info=True)
        error_payload = {
            'error' : {
                'code' : status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message' : 'Error interno del servidor',
                'details' : str(exc) if str(exc) else 'Contacte al administrador'
            }
        }
        response = Response(error_payload, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return response