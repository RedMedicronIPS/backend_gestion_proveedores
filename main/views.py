from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Funcionario, ContenidoInformativo, Evento, FelicitacionCumpleanios, Reconocimiento
from .serializers import (
    FuncionarioSerializer,
    ContenidoInformativoSerializer,
    EventoSerializer,
    FelicitacionCumpleaniosSerializer,
    ReconocimientoSerializer
)

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class ContenidoInformativoViewSet(viewsets.ModelViewSet):
    queryset = ContenidoInformativo.objects.all()
    serializer_class = ContenidoInformativoSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class FelicitacionCumpleaniosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FelicitacionCumpleanios.objects.all()
    serializer_class = FelicitacionCumpleaniosSerializer

class ReconocimientoViewSet(viewsets.ModelViewSet):
    queryset = Reconocimiento.objects.all().order_by('-fecha')
    serializer_class = ReconocimientoSerializer
