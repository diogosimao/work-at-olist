from django.conf.urls import url, include
from rest_framework import routers

from .views import ChannelViewSet


router = routers.SimpleRouter(trailing_slash=False)
router.register('channels', ChannelViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

