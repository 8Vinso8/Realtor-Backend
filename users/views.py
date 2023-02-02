from rest_framework import viewsets
from rest_framework import permissions
from users.models import CustomUser
from users.permissions import IsOwnerOrReadOnly
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly]

    