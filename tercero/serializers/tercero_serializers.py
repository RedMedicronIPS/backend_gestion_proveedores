from rest_framework import serializers
from ..models.terceros import Terceros

class TerceroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terceros
        fields = '_all_'