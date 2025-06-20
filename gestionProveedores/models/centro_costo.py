from django.db import models

class CentroCostos(models.Model):
    costos_id = models.AutoField(primary_key=True)
    costos_nombre_sede = models.CharField(max_length=250, default="")
    costos_estado = models.BooleanField(default=True)

    def __str__(self):
        return f"Centro de costos: {self.costos_nombre_sede}"
    class Meta:
        verbose_name = "Centro de costo"
        verbose_name_plural = "CENTRO DE COSTOS"