from django.db import models
from .factura import Factura

class RevisionImpuestos(models.Model):
    revision_impuestos_id = models.AutoField(primary_key=True)
    revision_impuestos_estado_impuestos =  models.IntegerField(default=0)
    revision_impuestos_observaciones = models.TextField(blank=True, null=True)
    revision_impuestos_estado = models.BooleanField(default=True)

    factura = models.ForeignKey(
        Factura,
        on_delete=models.CASCADE,
        null=False,
        related_name='etapas_impuestos'
    )

    def __str__(self):
        return f"Revision de impuestos de la factura con ID: {self.factura.factura_id}"
    class Meta:
        verbose_name = "Revisión impuestos"
        verbose_name_plural = "REVISIÓN IMPUESTOS"