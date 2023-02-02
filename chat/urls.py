from django.urls import path, include
from rest_framework import routers
from chat import views

router = routers.DefaultRouter()
router.register(r'', views.MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
