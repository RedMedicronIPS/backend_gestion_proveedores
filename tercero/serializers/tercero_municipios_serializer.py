from rest_framework import serializers
from ..models.tercero_municipios_serializer import Municipio

class TerceroMunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '_all_'