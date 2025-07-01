from django.contrib import admin
from .models import Terceros
from .models import Pais
from .models import Departamento
from .models import Municipio

@admin.register(Terceros)
class TercerosAdmin(admin.ModelAdmin):
    list_display = ('tercero_nombres', 'tercero_apellidos', 'tercero_email', 'tercero_tipo')
    search_fields = ('tercero_nombres', 'tercero_apellidos', 'tercero_email')


@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('pais_id', 'pais_nombre')
    search_fields = ( 'id','pais_id', 'pais_nombre')
    


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('departamento_id', 'departamento_nombre', 'departamento_pais')
    search_fields = ( 'id','departamento_id', 'departamento_nombre', 'departamento_pais')


@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('municipio_id', 'municipio_nombre', 'municipio_departamento')
    search_fields = ( 'id','municipio_id', 'municipio_nombre', 'municipio_departamento')