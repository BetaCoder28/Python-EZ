from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions


from django.contrib import admin
from django.urls import path, include
from apps.core.views import CookieTokenObtainPairView, CookieTokenRefreshView, LogoutView


# Enrutamiento principal
urlpatterns = [
    #Admin
    path('admin/', admin.site.urls),
    #Browsable API
    path('api-auth/', include('rest_framework.urls')),
    #Auth JWT
    path('api/v1/auth/login/', CookieTokenObtainPairView.as_view(), name='cookie_token_obtain_pair'),
    path('api/v1/auth/refresh/', CookieTokenRefreshView.as_view(), name='cookie_token_refresh'),
    path('api/v1/auth/logout/', LogoutView.as_view(), name='token_logout'),
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

