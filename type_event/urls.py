from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('evento/', include('eventos.urls')),
    path("", lambda request: redirect('/usuarios/cadastro')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
