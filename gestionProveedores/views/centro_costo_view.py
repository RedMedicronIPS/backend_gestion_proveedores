from rest_framework import viewsets
from ..models.centro_costo import CentroCostos
from ..serializers import CentroCostosSerializer

class CentroCostosViewSet(viewsets.ModelViewSet):
    queryset = CentroCostos.objects.all()
    serializer_class = CentroCostosSerializer
