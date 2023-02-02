from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'url', 'username', 'email', 'phone', 'favorite_adverts', 'is_realtor', 'clients']
        
