from rest_framework import serializers
from .models import Funcionario, ContenidoInformativo, Evento, FelicitacionCumpleanios, Reconocimiento

class FuncionarioSerializer(serializers.ModelSerializer):
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
