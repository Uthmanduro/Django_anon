from .models import Message
from rest_framework import serializers
from django.contrib.auth.models import User

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.CharField(max_length=255, required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']