from django.db import models
from .factura import Factura

class PendienteReconocimientoContable(models.Model):
    contable_id = models.AutoField(primary_key=True)
    contable_NIT_prestador = models.CharField(max_length=150, default="")    
    contable_estado = models.BooleanField(default=True)

    factura = models.ForeignKey(
    Factura,
    on_delete=models.CASCADE,
    null=False,
    related_name='etapas_contables'
)
    def __str__(self):
        return f"Pendiente de reconocimiento contable de la factura con ID: {self.factura.factura_id}"
    class Meta:
        verbose_name = "Pendiente reconocimiento contable"
        verbose_name_plural = "PENDIENTES RECONOCIMIENTOS CONTABLES"