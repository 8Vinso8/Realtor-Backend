from django.contrib.auth.models import User
from rest_framework import serializers
from advert.serializers import AdvertSerializer

from users.models import CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    favorite_adverts = AdvertSerializer(many=True, read_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'url', 'username', 'email', 'phone', 'favorite_adverts', 'is_realtor', 'clients', 'avatar']
        
