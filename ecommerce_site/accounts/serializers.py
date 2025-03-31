from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class meta:
        model = CustomUser
        field = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username = self.validated_data['username']
            email = self.validated_data['email']
            password = self.validated_data['password']
        )
        token, created = Token.objects.create(user=user)