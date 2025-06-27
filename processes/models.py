from django.db import models
from django.core.exceptions import ValidationError
from companies.models.process import Process

# === Constantes para tipos y estados ===
TIPOS_DOCUMENTO = [
    ('FC', 'Ficha de caracterización'),
    ('MA', 'Matriz'),
    ('PR', 'Procedimiento'),
    ('DI', 'Documento interno'),
    ('GU', 'Guía'),
    ('PT', 'Protocolo'),
    ('PL', 'Plan'),
    ('IN', 'Instructivo'),
    ('FR', 'Formato'),
    ('DE', 'Documento externo'),
]

ESTADOS = [
    ('VIG', 'Vigente'),
    ('OBS', 'Obsoleto'),
]

# === Validaciones ===
from django.core.exceptions import ValidationError

def validar_archivo_oficial(file):
    ext = file.name.lower().split('.')[-1]
    if ext not in ['pdf', 'xls', 'xlsx']:
        raise ValidationError("El archivo oficial debe ser PDF o Excel (.xls, .xlsx)")

def validar_archivo_editable(file):
    ext = file.name.lower().split('.')[-1]
    if ext not in ['doc', 'docx', 'xls', 'xlsx']:
        raise ValidationError("El archivo editable debe ser Word o Excel (.doc, .docx, .xls, .xlsx)")


# === Modelo principal ===
class Documento(models.Model):
    documento_padre = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL, related_name='versiones'
    )
    codigo_documento = models.CharField(max_length=50)
    nombre_documento = models.CharField(max_length=255)
    proceso = models.ForeignKey(Process, on_delete=models.PROTECT)
    tipo_documento = models.CharField(max_length=3, choices=TIPOS_DOCUMENTO)
    version = models.PositiveIntegerField()
    estado = models.CharField(max_length=3, choices=ESTADOS)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    archivo_oficial = models.FileField(
    upload_to='documentos/oficiales/',
    validators=[validar_archivo_oficial],
    null=False,
    blank=False
    )

    archivo_editable = models.FileField(
        upload_to='documentos/editables/',
        validators=[validar_archivo_editable],
        null=True,
        blank=True
    )


    class Meta:
        unique_together = ('codigo_documento', 'version')
        indexes = [
            models.Index(fields=['codigo_documento']),
            models.Index(fields=['tipo_documento']),
            models.Index(fields=['estado']),
        ]

    def __str__(self):
        return f"{self.codigo_documento} v{self.version} - {self.nombre_documento}"

    def get_ultima_version(self):
        return self.versiones.order_by('-version').first()

    