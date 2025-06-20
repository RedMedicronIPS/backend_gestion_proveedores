from rest_framework import viewsets
from ..models.terceros import Terceros
from ..serializers.tercero_paises_serializers import TerceroPaisesSerializer

class TerceroViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = TerceroPaisesSerializer








