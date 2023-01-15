from advert.models import Advert
from rest_framework import serializers


class AdvertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advert
        fields = ['id','url', 'owner', 'price', 'preview',
                  'address', 'description', 'date']
