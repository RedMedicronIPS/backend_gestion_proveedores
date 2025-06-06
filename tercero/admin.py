from django.contrib import admin
from .models import Tercero

@admin.register(Tercero)
class TerceroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_documento', 'numero_documento', 'correo')
    search_fields = ('nombre', 'numero_documento', 'correo')
