from rest_framework import serializers
from ..models import Result
from companies.models.headquarters import Headquarters
from users.models import User
from ..models.indicator import Indicator

class HeadquartersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headquarters
        fields = ['id', 'name', 'habilitationCode', 'city', 'address']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicator
        fields = ['id', 'name', 'code', 'version', 'calculationMethod', 'measurementUnit', 'target']

class ResultSerializer(serializers.ModelSerializer):
    headquarters = HeadquartersSerializer(read_only=True)
    indicator = IndicatorSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    
    # Para escritura
    headquarters_id = serializers.PrimaryKeyRelatedField(
        queryset=Headquarters.objects.all(), 
        source='headquarters', 
        write_only=True
    )
    indicator_id = serializers.PrimaryKeyRelatedField(
        queryset=Indicator.objects.all(), 
        source='indicator', 
        write_only=True
    )
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), 
        source='user', 
        write_only=True
    )
    
    class Meta:
        model = Result
        fields = [
            'id', 
            'headquarters', 
            'indicator', 
            'user',
            'headquarters_id',
            'indicator_id', 
            'user_id',
            'numerator', 
            'denominator', 
            'calculatedValue',
            'creationDate', 
            'updateDate',
            'year', 
            'month', 
            'quarter', 
            'semester'
        ]
        read_only_fields = ['calculatedValue', 'creationDate', 'updateDate']
