from advert.models import Advert, AdvertImage
from rest_framework import serializers


class ImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdvertImage
        fields = ['image']


class AdvertSerializer(serializers.HyperlinkedModelSerializer):
    images = ImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Advert
        fields = ['id', 'url', 'owner', 'price', 'preview',
                  'address', 'description', 'date', 'images']
