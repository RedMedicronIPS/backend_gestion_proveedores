from django.db import models
from .factura import Factura

class RevisionContraloria(models.Model):
    contraloria_id = models.AutoField(primary_key=True)
    contraloria_estado_contraloria = models.IntegerField(default=0)
    contraloria_observaciones = models.TextField(blank=True, null=True)
    contraloria_estado = models.BooleanField(default=True)

    factura = models.ForeignKey(
        Factura,
        on_delete=models.CASCADE,
        null=False,
        related_name='etapas_contraloria'
    )

    def __str__(self):
        return f"Revision por contraloria de la factura con ID: {self.factura.factura_id}"
    class Meta:
        verbose_name = "Revisión contraloría"
        verbose_name_plural = "REVISIÓN CONTRALORÍAS"