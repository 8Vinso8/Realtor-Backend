from advert.models import Advert
from rest_framework import viewsets
from rest_framework import permissions
from users.permissions import IsOwnerOrReadOnly
from advert.serializers import AdvertSerializer
from advert.filters import AdvertFilter
from rest_framework.response import Response

class AdvertViewSet(viewsets.ModelViewSet):
    queryset = Advert.objects.all().order_by('date')
    serializer_class = AdvertSerializer
    permission_classes = [IsOwnerOrReadOnly,
                          permissions.IsAuthenticatedOrReadOnly]
    filterset_class = AdvertFilter
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        favorite = self.request.query_params.get('favorite')
        user = self.request.user

        if favorite == "true":
            user.favorite_adverts.add(instance)
        if favorite == "false":
            user.favorite_adverts.remove(instance)
            
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    
