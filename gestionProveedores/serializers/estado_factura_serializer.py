from rest_framework import serializers
from gestionProveedores.models.estado_factura import EstadoFactura

class EstadoFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoFactura
        fields = '__all__'
