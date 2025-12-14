from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions


from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


# Enrutamiento principal
urlpatterns = [
    #Admin
    path('admin/', admin.site.urls),
    #Browsable API
    path('api-auth/', include('rest_framework.urls')),
    #Auth JWT
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    #API URLS
    path('api/v1/', include('apps.authors.urls')),
    path('api/v1/',include('apps.genres.urls')),
    path('api/v1/',include('apps.books.urls')),
    path('api/v1/', include('apps.users.urls')),
]


# En desarrollo sirve archivos media y habilita debug toolbar
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Debug Toolbar
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns

