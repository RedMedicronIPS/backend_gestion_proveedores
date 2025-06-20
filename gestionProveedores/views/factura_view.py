from rest_framework import viewsets
from ..models.factura import Factura
from ..serializers import FacturaSerializer

class FacturaViewSet(viewsets.ModelViewSet): 
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
