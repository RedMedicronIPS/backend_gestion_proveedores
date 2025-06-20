from rest_framework import viewsets
from ..models.revision_contraloria import RevisionContraloria
from ..serializers import RevisionContraloriaSerializer

class RevisionContraloriaViewSet(viewsets.ModelViewSet): 
    queryset = RevisionContraloria.objects.all()
    serializer_class = RevisionContraloriaSerializer
