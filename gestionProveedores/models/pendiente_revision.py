from django.db import models
from .factura import Factura

class PendienteRevision(models.Model):
    revision_id = models.AutoField(primary_key=True)
    revision_fecha_gestion = models.DateField(null=True, blank=True)
    revision_fecha_recibe = models.DateField(null=True, blank=True)
    revision_estado = models.BooleanField(default=True)

    factura = models.ForeignKey(
        Factura,
        on_delete=models.CASCADE,
        null=False,
        related_name='etapas_revision'
    )

    def __str__(self):
        return f"Pendiente de revisión de la factura con ID: {self.factura.factura_id}"
    class Meta:
        verbose_name = "Pendiente Revisión"
        verbose_name_plural = "PENDIENTES REVISIÓN"