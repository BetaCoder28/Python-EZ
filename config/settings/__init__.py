import os
from .base import *

# Determinar que configuración cargar en base al entorno
environment = os.getenv('DJANGO_ENV', 'local').lower()

if environment == 'production':
    from .production import *
else:
    from .local import *




