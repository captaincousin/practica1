from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Plato)
admin.site.register(Trabajador)

class PlatoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'trabajador')
    list_filter = ('trabajador')
    search_fields = ('nombre', 'descripcion')