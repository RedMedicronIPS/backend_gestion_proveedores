from rest_framework import viewsets
from ..models.pendiente_revision import PendienteRevision
from ..serializers import PendienteRevisionSerializer

class PendienteRevisionViewSet(viewsets.ModelViewSet): 
    queryset = PendienteRevision.objects.all()
    serializer_class = PendienteRevisionSerializer
