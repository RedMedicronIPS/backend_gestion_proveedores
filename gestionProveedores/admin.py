from django.contrib import admin
from gestionProveedores.models.factura import Factura
from gestionProveedores.models.factura_detalle import FacturaElectronicaDetalle
from gestionProveedores.models.causal_devolucion import CausalDevolucion
from gestionProveedores.models.pendiente_revision import PendienteRevision
from gestionProveedores.models.pendiente_reconocimiento_contable import PendienteReconocimientoContable
from gestionProveedores.models.revision_impuestos import RevisionImpuestos
from gestionProveedores.models.revision_contraloria import RevisionContraloria
from gestionProveedores.models.centro_costo import CentroCostos
from gestionProveedores.models.centro_operaciones import CentroOperaciones
from django.urls import reverse
from django.utils.html import format_html

class FacturaElectronicaDetalleInline(admin.StackedInline):  # ← cambia aquí
    model = FacturaElectronicaDetalle
    extra = 0
    fieldsets = [
        (None, {
            'fields': [
                'descripcionFactura',
                'observacionesGestion',
                'observacionesInconsistencias',
                'observacionesConformidad',
                'observacionesPago',
                'observacionesContabilidad',
                'observacionesRevision',
                'observacionesImpuestos',
                'observacionesContraloria',     
            ]
        }),
    ]

@admin.register(CausalDevolucion)
class CausalDevolucionAdmin(admin.ModelAdmin):
    list_display = ['causalid', 'causal_nombre', 'causal_fecha', ]

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = [
        'factura_id',
        'factura_centro_operaciones',
        'factura_etapa',
        'factura_fecha',
        'factura_estado_factura',
        'factura_numero_autorizacion',
        'factura_concepto',
        'factura_razon_social_proveedor',
        'factura_razon_social_adquiriente',
    ]


    readonly_fields = ['factura_id']

    
    fields = [
        'factura_id',
        'factura_id_factura_electronica',
        'factura_etapa',
        'factura_fecha',
        'factura_estado_factura',
        'factura_numero_autorizacion',
        'factura_concepto',
        'factura_razon_social_proveedor',
        'factura_razon_social_adquiriente',
        'factura_valor',
        'factura_centro_operaciones',
        'factura_centro_costo',
        'causal_anulacion',
        'causal_contabilidad',
        'causal_revision',
        'causal_impuestos',
    ]

    inlines = [FacturaElectronicaDetalleInline]
@admin.register(PendienteRevision)
class PendienteRevisionAdmin(admin.ModelAdmin):
    list_display = ['revision_id', 'revision_fecha_gestion', 'revision_fecha_recibe', 'revision_estado',]
@admin.register(PendienteReconocimientoContable)
class PendienteReconocimientoContableAdmin(admin.ModelAdmin):
    list_display = ['contable_id', 'contable_NIT_prestador', 'contable_estado', ]
@admin.register(RevisionImpuestos)
class RevisionImpuestosAdmin(admin.ModelAdmin):
    list_display = ['revision_impuestos_id', 'revision_impuestos_estado_impuestos', 'revision_impuestos_observaciones', 'revision_impuestos_estado',]
@admin.register(RevisionContraloria)
class RevisionContraloriaAdmin(admin.ModelAdmin):
    list_display = ['contraloria_id', 'contraloria_estado_contraloria', 'contraloria_observaciones', 'contraloria_estado',]
    
@admin.register(CentroCostos)
class CentroCostoAdmin(admin.ModelAdmin):
    list_display = ['costos_id', 'costos_nombre_sede', 'costos_estado',]
@admin.register(CentroOperaciones)
class CentroOperacionesAdmin(admin.ModelAdmin):
    list_display = ['operaciones_id', 'operaciones_nombre', 'operaciones_estado',]
