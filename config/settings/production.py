# CONFIGURATION PARA PRODUCCIÓN
from .base import *

# SECURTITY SETTINGs
DEBUG = False

# SECURITY HEADERS
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
# SSL OBLIGATORIO
# Cookies seguras, solo se transmiten por https


# DATABASE - PSQL EN PRODUCCIÓN
DATABASES['default'] = dj_database_url.config(
    default = config('DATABASE_URL'),
    conn_max_age=600, #Conexiones por 10 minutos
    ssl_require=True
)

# STATIC FILES WHITENOISE
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware', #Servir archivos estaticos eficientemente
] + MIDDLEWARE

STATICSFILES_STORAGE = 'whitenoise.storage.CompresseManifestStaticFilesStorage'

# LOGGING - PRODUCCIóN
LOGGING = {
    'version' : 1,
    'disable_existing_loggers' : False,
    'handlers' : {
        'file' : {
            'level' : 'ERROR',
            'class' : 'logging.FileHandler',
            'filename' : BASE_DIR / 'logs' / 'django.log',
        },
    },
    'loggers' : {
        'django' : {
            'handlers' : ['file'],
            'level' : 'ERROR',
            'propagate' : True,
        },
    },
}