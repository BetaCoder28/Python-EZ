# Configuración para entorno de desarrollo local
from .base import *

# DEBUG CONFIGURATION
DEBUG = True #Muestra errores detallados

# DATABASE
DATABASES['default'] = {
    'ENGINE' : 'django.db.backends.sqlite3',
    'NAME' : BASE_DIR / 'db.sqlite3'
}

# DEBUG TOOLBAR
if config('ENABLE_DEBUG_TOOLBAR', default=True, cast=bool): #Herramienta de debugging en desarrollo
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE
    INTERNAL_IPS = ['127.0.0.1']
#DEBUG TOOLBAR -> Herramienta de diagnostico, muestra info de SQL, tiempo de respuesta, etc


# REST FRAMEWORK + MÁS DETALLES EN DESARROLLO
REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
    'rest_framework.renderers.JSONRenderer',
    'rest_framework.renderers.BrowsableAPIRenderer' #Solo en desarrollo -> Interfaz web navegable
]

# EMAIL- CONSOLA EN DESARROLLO
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# LOGGING- DETALLADO EN DESARROLLO
LOGGING = {
    'version' : 1,
    'disable_existing_loggers' : False,
    'handlers' : {
        'console' : {
            'class' : 'logging.StreamHandler'
        },
    },
    'root' : {
        'handlers' : ['console'],
        'level' : 'INFO'
    },
    'loggers' : {
        'django' : {
            'handlers' : ['console'],
            'level' : 'INFO',
            'propagate' : False
        }
    }
}




