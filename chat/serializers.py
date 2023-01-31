from django.conf import settings

from rest_framework import serializers

from chat.models import Message


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(
        many=False, slug_field='username', queryset=settings.AUTH_USER_MODEL.objects.all())
    receiver = serializers.SlugRelatedField(
        many=False, slug_field='username', queryset=settings.AUTH_USER_MODEL.objects.all())

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver',
                  'message', 'timestamp', 'is_read']
