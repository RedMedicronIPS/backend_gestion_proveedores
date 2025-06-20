from django.db import models

class DocumentoContable(models.Model):
    doc_contable_id = models.AutoField(primary_key=True)
    doc_contable_tipo = models.CharField(max_length=250, default="")
    doc_contable_descripcion = models.TextField(blank=True, null=True)
    doc_contable_estado=  models.BooleanField(default=True)
    
    def __str__(self):
        return f"Documento contable: {self.operaciones_nombre}"
    class Meta:
        verbose_name = "Documento contable"
        verbose_name_plural = "DOCUMENTOS CONTABLES"