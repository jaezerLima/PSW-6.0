from django.contrib import admin
from .models import Evento
# Register your models here.

admin.site.register(Evento)

def __str__(self):
    return self.nome