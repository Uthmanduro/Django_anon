from django.shortcuts import render
from .models import Message
from .serializers import MessageSerializer
from rest_framework import generics
# Create your views here.

class MessageAPI(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer