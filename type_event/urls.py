from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('evento/', include('eventos.urls')),
    path("", lambda request: redirect('/usuarios/cadastro')),
]
