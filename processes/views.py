from django.shortcuts import render
from rest_framework import viewsets
from .models import Documento
from .serializers import DocumentoSerializer

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all().order_by('-fecha_actualizacion')
    serializer_class = DocumentoSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']