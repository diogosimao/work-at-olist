from django.conf.urls import url, include

from .views import ChannelViewSet, ChannelCategoriesViewSet


urlpatterns = [
    url(r'^channels/', ChannelViewSet.as_view()),
    url(r'^channel/(?P<slug>[^/.]+)$', ChannelCategoriesViewSet.as_view()),
]

