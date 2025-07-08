from rest_framework import serializers
from .models import Funcionario, ContenidoInformativo, Evento, FelicitacionCumpleanios, Reconocimiento
from companies.models.headquarters import Headquarters

class HeadquartersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headquarters
        fields = ['id', 'name', 'habilitationCode', 'city', 'address']

class FuncionarioSerializer(serializers.ModelSerializer):
    sede = HeadquartersSerializer(read_only=True)
    sede_id = serializers.PrimaryKeyRelatedField(
        queryset=Headquarters.objects.all(), source="sede", write_only=True
    )
    
    class Meta:
        model = Funcionario
        fields = '__all__'

class ContenidoInformativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContenidoInformativo
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class FelicitacionCumpleaniosSerializer(serializers.ModelSerializer):
    funcionario = FuncionarioSerializer(read_only=True)

    class Meta:
        model = FelicitacionCumpleanios
        fields = '__all__'

class ReconocimientoSerializer(serializers.ModelSerializer):
    funcionario = FuncionarioSerializer(read_only=True)
    funcionario_id = serializers.PrimaryKeyRelatedField(
        queryset=Funcionario.objects.all(), source="funcionario", write_only=True
    )

    class Meta:
        model = Reconocimiento
        fields = '__all__'
