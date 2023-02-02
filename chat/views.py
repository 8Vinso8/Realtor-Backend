from django.shortcuts import render

from chat.models import Message
from chat.serializers import MessageSerializer
from rest_framework import viewsets, permissions

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('timestamp')
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
