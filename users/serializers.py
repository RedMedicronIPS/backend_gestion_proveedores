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
        fields = ['id', 'username', 'email', 'role']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            token = RefreshToken.for_user(user)
            return {
                'user': UserSerializer(user).data,
                'refresh': str(token),
                'access': str(token.access_token),
            }
        raise serializers.ValidationError("Invalid credentials")
