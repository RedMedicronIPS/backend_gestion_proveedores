from django.contrib import admin
from .models import Terceros

@admin.register(Terceros)
class TercerosAdmin(admin.ModelAdmin):
    list_display = ('tercero_nombres', 'tercero_apellidos', 'tercero_email', 'tercero_tipo')
    search_fields = ('tercero_nombres', 'tercero_apellidos', 'tercero_email')