from rest_framework import viewsets
from ..models.causal_devolucion import CausalDevolucion
from ..serializers import CausalDevolucionSerializer

class CausalDevolucionViewSet(viewsets.ModelViewSet):
    queryset = CausalDevolucion.objects.all()
    serializer_class = CausalDevolucionSerializer
