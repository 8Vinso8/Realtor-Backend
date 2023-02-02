from django.conf import settings

from rest_framework import serializers

from chat.models import Message

from django.contrib.auth import get_user_model


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(
        many=False, slug_field='username', queryset=get_user_model().objects.all())
    receiver = serializers.SlugRelatedField(
        many=False, slug_field='username', queryset=get_user_model().objects.all())

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver',
                  'message', 'timestamp', 'is_read']
