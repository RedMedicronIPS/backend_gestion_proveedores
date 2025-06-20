from rest_framework import viewsets
from ..models.factura_detalle import FacturaElectronicaDetalle
from ..serializers import FacturaElectronicaDetalleSerializer

class FacturaDetalleViewSet(viewsets.ModelViewSet):
    queryset = FacturaElectronicaDetalle.objects.all()
    serializer_class = FacturaElectronicaDetalleSerializer
