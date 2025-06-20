from rest_framework import viewsets
from ..models.pendiente_reconocimiento_contable import PendienteReconocimientoContable
from ..serializers import PendienteReconocimientoContableSerializer

class PendienteReconocimientoContableViewSet(viewsets.ModelViewSet): 
    queryset = PendienteReconocimientoContable.objects.all()
    serializer_class = PendienteReconocimientoContableSerializer
