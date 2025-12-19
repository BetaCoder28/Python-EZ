# Base configuration shared with all environments
from datetime import timedelta
import os
from pathlib import Path
from decouple import config, Csv # Usa python decouple para leer variables de entorno
import dj_database_url

# Define el directorio base del proyecto(NIVEL SUPERIOR)
# Path(__file__) -> Obtiene la ruta absoluta del archivo actual
# .parent.parent sube dos niveles desde settings/base.py 
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY SETTINGS
SECRET_KEY = config('SECRET_KEY', default='clave-por-defecto') #clave cripto para seguridad de django
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=Csv()) #Dominios permitidos para servir el API

AUTH_USER_MODEL = 'users.CustomUser'

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] #APPS NATIVAS DE DJANGO

THIRD_PARTY_APPS = [
    'rest_framework',
    'django_filters',
    'corsheaders',
    'drf_yasg', #Doc automatica con swagger
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist'
] #APPS EXTERNAS

LOCAL_APPS = [
    'apps.core',
    'apps.authors',
    'apps.genres',
    'apps.books',
    'apps.users',
] #APPS DEL PROYECTO

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE
# Cada middleware procesa request/response en orden
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', #Middleware de cors
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'apps.core.middleware.JWTCookieMiddleware', #Middleware de cookies JWT
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL CONFIGURATION
ROOT_URLCONF = 'config.urls'

# TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# DATABASES
# SOPORTE PARA database_url (heroku, docker, aws, etc)
DATABASE_URL = config('DATABASE_URL', default=None)
if DATABASE_URL:
    DATABASES = {
        'default' : dj_database_url.config(
            default=DATABASE_URL, 
            conn_max_age=600,
            ssl_require=config('DB_SSL_REQUIRE', default=False, cast=bool)
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': config('DB_ENGINE', default='django.db.backends.sqlite3'),
            'NAME': config('DB_NAME', default = BASE_DIR / 'db.sqlite3'),
            'USER' : config('DB_USER', default = ''),
            'PASSWORD' : config('DB_PASSWORD', default = ''),
            'HOST' : config('DB_HOST', default = ''),
            'PORT' : config('DB_PORT', default = ''),
        }
    }

# REST_FRAMEWORK

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS' : 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE' : 20, #PAGINACIÓN divide resultados en paginas de 20 elementos
    'DEFAULT_FILTER_BACKENDS' : [
        'django_filters.rest_framework.DjangoFilterBackend',#Filtrado por campos
        'rest_framework.filters.SearchFilter', #Busqueda textual
        'rest_framework.filters.OrderingFilter', #Ordenamiento
    ],
    'DEFAULT_PERMISSION_CLASSES' : [
        'rest_framework.permissions.IsAuthenticated'
    ], # Requiere autenticación por defecto
    'DEFAULT_AUTHENTICATION_CLASSES' : [
        'apps.core.authentication.JWTCookieAuthentication', #Autenticación por cookies
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'EXCEPTION_HANDLER' : 'apps.core.exceptions.custom_exception_handler', #Respuestas de error consistentes
    'DEFAULT_SCHEMA_CLASS' : 'rest_framework.schemas.coreapi.AutoSchema'
}

# Internacionalization
LANGUAGE_CODE = 'es-MX'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True #Internacionalización para manejar diferentes idiomas
USE_TZ  = True #Soporte para zonas horarias


#STATIC FILES
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICSFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


#DEFAULT PRIMARY KEY
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CONTROLAR QUE SITIOS PUEDEN HACER REQUESTS

# CORS SETTINGS
CORS_ALLOWED_ORIGINS = config(
    'CORS_ALLOWED_ORIGINS',
    default='http://localhost:3000,http://127.0.0.1:3000',
    cast=Csv()
) #Origenes especificos permitidos

# permite enviar cookies en CORS
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_ALL_ORIGINS = config('CORS_ALLOW_ALL_ORIGINS', default=False, cast=bool)

# JWT CONFIGURATION
SIMPLE_JWT = {
    # Tiempos de vida
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=config('JWT_ACCESS_TOKEN_LIFETIME_MINUTES',default=15, cast=int)),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=config('JWT_REFRESH_TOKEN_LIFETIME_DAYS',default=1, cast=int)),
    # Cambiar y bloquear tokens después de usar
    'ROTATE_REFRESH_TOKENS': config('JWT_ROTATE_REFRESH_TOKENS', default=True, cast=bool),
    'BLACKLIST_AFTER_ROTATION' : config('JWT_BLACKLIST_AFTER_ROTATION', default=True, cast=bool),
    #Algoritmo y firma para criptografía 
    'ALGORITHM' : config('JWT_ALGORITHM', default='HS256'),
    'SIGNING_KEY' : config('JWT_SIGNING_KEY', default=SECRET_KEY),
    # HEADER HTTP estándar para jwt
    # Permite-> Authorization: Bearer, JWT, Token
    'AUTH_HEADER_TYPES' : ('Bearer',),
    # Nombre del header
    'AUTH_HEADER_NAME' : 'HTTP_AUTHORIZATION',
    # campo del User elegido como id
    'USER_ID_FIELD' : 'id',
    # Id para el token
    'USER_ID_CLAIM' : 'user_id',
    # Seguridad en el navegador
    'AUTH_COOKIE' : 'access_token', #Nombre de la cookie de autenticación
    # False -> HTTP, True -> HTTPS
    'AUTH_COOKIE_SECURE' : not DEBUG,
    # NO MOSTRAR LAS COOKIES JWT en JS
    'AUTH_COOKIE_HTTP_ONLY' : True,
    # Permitir cookies desde diferentes sitios
    'AUTH_COOKIE_SAMESITE' : 'Lax',
    # Controla a qué rutas se envía la cookie
    'AUTH_COOKIE_PATH' : '/',
}


#CSRF SETTINGS -> protección contra CROSS SITE REQUEST FORGERY(falsificación de solicitudes entre sitios)
CSRF_TRUSTED_ORIGINS = config(
    'CSRF_TRUSTED_ORIGINS',
    default='http://localhost:8000,http://127.0.0.1:8000',
    cast=Csv()
)