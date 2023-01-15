from advert.models import Advert, AdvertImage
from rest_framework import serializers


class ImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdvertImage
        fields = ['image']


class AdvertSerializer(serializers.HyperlinkedModelSerializer):
    images = ImagesSerializer(many=True, read_only=True)
    phone = serializers.SerializerMethodField()

    def get_phone(self, obj):
        if obj.owner.phone:
            return obj.owner.phone
        return None

    class Meta:
        model = Advert
        fields = ['id', 'url', 'owner', 'price', 'preview',
                  'address', 'description', 'date', 'images', 'phone', 'title']
