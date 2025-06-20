from rest_framework import viewsets
from .models import Tercero
from .serializers import TerceroSerializer
from rest_framework.permissions import IsAuthenticated

class TerceroViewSet(viewsets.ModelViewSet):
    queryset = Tercero.objects.all()
    serializer_class = TerceroSerializer
    permission_classes = [IsAuthenticated]

