from django.conf.urls import url, include

from .views import ChannelView, ChannelCategoriesView


urlpatterns = [
    url(r'^channels/', ChannelView.as_view()),
    url(r'^channel/(?P<slug>[^/.]+)$', ChannelCategoriesView.as_view()),
]

