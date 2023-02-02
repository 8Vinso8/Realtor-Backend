from advert.models import Advert, AdvertImage
from rest_framework import serializers


class ImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdvertImage
        fields = ['image']


class AdvertSerializer(serializers.HyperlinkedModelSerializer):
    images = ImagesSerializer(many=True, read_only=True)
    phone = serializers.SerializerMethodField()
    is_favorite = serializers.SerializerMethodField()

    def get_phone(self, obj):
        if obj.owner.phone:
            return obj.owner.phone
        return None

    def get_is_favorite(self, obj):
        user = self.context.get('request').user
        if not user.is_authenticated:
            return False
        return user.favorite_adverts.filter(pk=obj.pk).exists()
    
    class Meta:
        model = Advert
        fields = ['id', 'url', 'advert_type', 'city', 'street', 'latitude', 'longitude', 'address', 'floor',  'owner', 'price', 'preview',
                  'address', 'description', 'date', 'images', 'phone', 'title', 'is_favorite', 'sold']
