from rest_framework import serializers
from ..models.tercero_departamento_serializer import Departamento

class TerceroDepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '_all_'