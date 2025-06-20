from rest_framework import viewsets
from ..models.revision_impuestos import RevisionImpuestos
from ..serializers import RevisionImpuestosSerializer

class RevisionImpuestosViewSet(viewsets.ModelViewSet): 
    queryset = RevisionImpuestos.objects.all()
    serializer_class = RevisionImpuestosSerializer
