# VARIABLES DE ENTORNO
## LOCAL
#### SEGURIDAD
DEBUG=True
SECRET_KEY=django-insecure-clave-super-secreta-para-desarrollo-2024
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

#### BASE DE DATOS (SQLite)
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

#### CORS - FRONTEND LOCAL
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000,http://localhost:5173
CORS_ALLOW_ALL_ORIGINS=False

#### CSRF
CSRF_TRUSTED_ORIGINS=http://localhost:8000,http://127.0.0.1:8000

#### DEBUG TOOLBAR
ENABLE_DEBUG_TOOLBAR=True

#### EMAIL (CONSOLA)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend

#### LOGGING LEVEL
LOG_LEVEL=DEBUG

## PROD
#### SEGURIDAD - CRÍTICO EN PRODUCCIÓN
DEBUG=False
SECRET_KEY=tu-clave-super-secreta-muy-larga-y-compleja-aqui-2024-prod
ALLOWED_HOSTS=midominio.com,www.midominio.com,api.midominio.com,tu-ip-del-servidor

#### BASE DE DATOS (PostgreSQL - RECOMENDADO)
DB_ENGINE=django.db.backends.postgresql
DB_NAME=mi_proyecto_db
DB_USER=mi_proyecto_user
DB_PASSWORD=tu-password-super-seguro-de-postgres-2024
DB_HOST=localhost
DB_PORT=5432

#### O ALTERNATIVAMENTE - URL DE BASE DE DATOS (para servicios cloud)
DATABASE_URL=postgres://mi_proyecto_user:tu-password-super-seguro-de-postgres-2024@localhost:5432/mi_proyecto_db

#### CORS - DOMINIOS PERMITIDOS EN PRODUCCIÓN
CORS_ALLOWED_ORIGINS=https://midominio.com,https://www.midominio.com,https://app.midominio.com
CORS_ALLOW_ALL_ORIGINS=False

#### CSRF - DOMINIOS SEGUROS
CSRF_TRUSTED_ORIGINS=https://midominio.com,https://www.midominio.com,https://api.midominio.com

#### DEBUG TOOLBAR (DESACTIVADO)
ENABLE_DEBUG_TOOLBAR=False

#### EMAIL PRODUCCIÓN
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=tu-email@gmail.com
EMAIL_HOST_PASSWORD=tu-app-password-de-gmail

#### SEGURIDAD ADICIONAL
SECURE_HSTS_SECONDS=31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=True

#### LOGGING
LOG_LEVEL=ERROR


# CREAR TODAS LAS MIGRACIONES
    python3 manage.py makemigrations
# CORRER TODAS LAS MIGRACIONES
    python3 manage.py migrate
# CORRER PROYECTO
    python3 manage.py runserver

# CREAR SUPERUSUARIO
    python3 manage.py createsuperuser
    
# CLASS META

- Clases internas que proporcionan metadatos (información sobre la clase) a Django. Su función varía según el contexto

## EN MODELOS
    * verbose_name -> Nombre legible en singular para el admin
    * vebose_name_plural -> Nombre en plural para el admin
    * ordering -> Orden por defecto al hacer consultas
    * db_table -> Nombre personalizado de la tabla en la bd
    * constraint -> Restricciones de BASE DE DATOS
    * indexes -> Indices para optimizar consultas

## EN SERIALIZERS
    * model -> modelo al que está asociado
    * fields -> campos que se incluyen en la serialización
    * exclude -> campos que se excluyen de la serialización
    * read_only_fields -> campos de solo lectura
    * extra_kwargs -> configuración adicional para campos específicos
    * depth -> profundidad de la serialización (para relaciones anidadas)

# QUERYSET
    * Define de donde se obtienen los objetos
    * Filtrado inicial -> que el objeto tenga is_active = True
    * Optimización -> puede incluir select_related o prefetch_related
        *select_related -> realiza un JOIN y obtiene los datos de las relaciones de un solo golpe(carga los objetos relacionados en la misma consulta)
        *prefetch_related -> para relaciones muchos a muchos -> pre carga de relaciones(no se puede hacer un JOIN DIRECTO)
    * Restringe que registros son accesibles

# VALIDATORS:
## Modelo -> Se activan cuando:
    * Se guarda en el admin de Django

## Serializer -> Se activan cuando:
    * Se crea o actualiza un objeto a través de la API
    * Se valida manualmente con serializer.is_valid()
    * Si se ejecutan automaticamente en las vistas de DRF

# MÉTODO  ->  __str__
### Método para representar el objeto como string
    * se activa en admin de DJANGO
    * shell de django
    * Logs y debugging

# ELIMINAR Y REACTIVAR (SOFT DELETE)
### DELETE /api/v1/author/1580/
    * La vista hace:
        * author.is_active = False
        * author.save()
    /* En el basemodel se muestra el funcionamiento de la función soft_delete */

### ACTIVAR
### USANDO EL ADMIN DE DJANGO xd
    * También se puede usar el endpoint patch con "is_active" = True
