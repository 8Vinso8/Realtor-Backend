from advert.models import Advert
from rest_framework import viewsets
from rest_framework import permissions
from users.permissions import IsOwnerOrReadOnly
from advert.serializers import AdvertSerializer


class AdvertViewSet(viewsets.ModelViewSet):
    queryset = Advert.objects.all().order_by('date')
    serializer_class = AdvertSerializer
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly]
