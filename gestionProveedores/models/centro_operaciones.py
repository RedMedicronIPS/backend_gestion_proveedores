from django.db import models

class CentroOperaciones(models.Model):
    operaciones_id = models.AutoField(primary_key=True)
    operaciones_nombre = models.CharField(max_length=250, default="")
    operaciones_estado = models.BooleanField(default=True)

    def __str__(self):
        return f"Centro de operaciones: {self.operaciones_nombre}"
    class Meta:
        verbose_name = "Centro de operacion"
        verbose_name_plural = "CENTRO DE OPERACIONES"