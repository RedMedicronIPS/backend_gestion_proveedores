from django.db import models
from .terceros_paises import Pais
from .terceros_departamentos import Departamento
from .terceros_municipios import Municipio



class Terceros(models.Model):
    tercero_id = models.AutoField(primary_key=True, verbose_name="ID Tercero")
    tercero_codigo = models.CharField(max_length=50, verbose_name="Código")
    tercero_nombres = models.CharField(max_length=100, verbose_name="Nombres")
    tercero_apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    tercero_razon_social = models.CharField(max_length=150, blank=True, null=True, verbose_name="Razón social")
    tercero_fecha_nacimiento = models.DateField(blank=True, null=True, verbose_name="Fecha de nacimiento")
    tercero_direccion = models.CharField(max_length=150, blank=True, null=True, verbose_name="Dirección")
    tercero_telefono = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono")
    tercero_email = models.EmailField(blank=True, null=True, verbose_name="Correo electrónico")

    tercero_pais = models.ForeignKey(
        Pais, on_delete=models.PROTECT, related_name='terceros_pais', verbose_name="País", blank=True, null=True
    )
    tercero_departamento = models.ForeignKey(
        Departamento, on_delete=models.PROTECT, related_name='terceros_departamento', verbose_name="Departamento", blank=True, null=True
    )
    tercero_municipio = models.ForeignKey(
        Municipio, on_delete=models.PROTECT, related_name='terceros_municipio', verbose_name="Municipio", blank=True, null=True
    )

    tercero_obligado_facturar = models.BooleanField(default=False, verbose_name="Obligado a facturar", null=True)
    tercero_proveedor = models.BooleanField(default=False, verbose_name="Proveedor", null=True)
    tercero_tipo = models.BooleanField(default=False, verbose_name="Tipo tercero", null=True)

    tercero_estado = models.BooleanField(default=True, verbose_name="Estado", null=True)

    def __str__(self):
        return f"{self.tercero_nombres} {self.tercero_apellidos}"

    class Meta:
        verbose_name = "Tercero"
        verbose_name_plural = "TERCEROS"
