from rest_framework import serializers
from gestionProveedores.models.revision_impuestos import RevisionImpuestos

class RevisionImpuestosSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevisionImpuestos
        fields = '__all__'

from rest_framework import serializers
from gestionProveedores.models.factura import Factura
from .causal_devolucion_serializer import CausalDevolucionSerializer
from .factura_detalle_serializer import FacturaElectronicaDetalleSerializer
from .pendiente_revision_serializer import PendienteRevisionSerializer


