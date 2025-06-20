from rest_framework import viewsets
from ..models.centro_operaciones import CentroOperaciones
from ..serializers import CentroOperacionesSerializer

class CentroOperacionesViewSet(viewsets.ModelViewSet):
    queryset = CentroOperaciones.objects.all()
    serializer_class = CentroOperacionesSerializer
