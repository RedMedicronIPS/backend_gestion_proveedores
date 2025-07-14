from rest_framework import serializers
from ..models.indicator import Indicator
from companies.models.process import Process as ProcessModel
from users.models import User as UserModel

class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessModel
        fields = ['id', 'name', 'description']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class IndicatorSerializer(serializers.ModelSerializer):
    Process = ProcessSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    
    # Para escritura
    process_id = serializers.PrimaryKeyRelatedField(
        queryset=ProcessModel.objects.all(),
        source='Process', 
        write_only=True
    )
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=UserModel.objects.all(),
        source='user', 
        write_only=True
    )
    
    class Meta:
        model = Indicator
        fields = [
            'id',
            'name',
            'description', 
            'code',
            'version',
            'calculationMethod',
            'measurementUnit',
            'numerator',
            'numeratorResponsible',
            'numeratorSource',
            'numeratorDescription',
            'denominator',
            'denominatorResponsible',
            'denominatorSource',
            'denominatorDescription',
            'trend',
            'target',
            'author',
            'Process',
            'measurementFrequency',
            'status',
            'user',
            'process_id',
            'user_id',
            'creationDate',
            'updateDate'
        ]
        read_only_fields = ['creationDate', 'updateDate']