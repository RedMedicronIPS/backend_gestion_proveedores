from django.db import models

class CausalDevolucion(models.Model):
    causalid = models.AutoField(primary_key=True)
    causal_nombre = models.CharField(max_length=200, default="")
    causal_fecha = models.DateField(null=True, blank=True)
    causal_estado = models.BooleanField(default=True)

    def __str__(self):
        return self.causal_nombre
    class Meta:
        verbose_name = "Causal Devolución"
        verbose_name_plural = "CAUSAL DEVOLUCIONES"