from rest_framework import serializers
from gestionProveedores.models.pendiente_revision import PendienteRevision

class PendienteRevisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PendienteRevision
        fields = '__all__'

