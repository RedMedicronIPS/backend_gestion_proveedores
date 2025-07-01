from rest_framework import serializers
from gestionProveedores.models.factura import Factura
from .causal_devolucion_serializer import CausalDevolucionSerializer
from .factura_detalle_serializer import FacturaElectronicaDetalleSerializer
from .etapa1_gestion_FE_serializer import GestionarFESerializer
from .etapa2_pendiente_revision_serializer import PendienteRevisionSerializer
from .etapa3_pendiente_reconocimiento_contable_serializer import PendienteReconocimientoContableSerializer

class FacturaSerializer(serializers.ModelSerializer):
    causal_anulacion = CausalDevolucionSerializer(read_only=True)
    causal_contabilidad = CausalDevolucionSerializer(read_only=True)
    causal_revision = CausalDevolucionSerializer(read_only=True)
    causal_impuestos = CausalDevolucionSerializer(read_only=True)
    detalles = FacturaElectronicaDetalleSerializer(many=True, read_only=True)
    pendiente_revision = PendienteRevisionSerializer(many=True, read_only=True)
    pendiente_reconocimiento_contable = PendienteReconocimientoContableSerializer(many=True, read_only=True)
    class Meta:
        model = Factura
        fields = '__all__'
