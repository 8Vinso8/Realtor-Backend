from django.urls import path, include
from rest_framework import routers
from advert import views

router = routers.DefaultRouter()
router.register(r'', views.AdvertViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
