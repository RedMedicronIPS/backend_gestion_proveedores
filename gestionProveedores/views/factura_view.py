from django.shortcuts import render
from rest_framework import viewsets
from ..models import Factura
from ..serializers import FacturaSerializer
from rest_framework.permissions import IsAuthenticated

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    permission_classes = [IsAuthenticated]
