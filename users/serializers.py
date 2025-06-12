from rest_framework import serializers
from .models import User, Role
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'is_2fa_enabled']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    otp_code = serializers.CharField(required=False)

    def validate(self, attrs):
        # Remover la validación aquí ya que se hará en la vista
        return attrs
