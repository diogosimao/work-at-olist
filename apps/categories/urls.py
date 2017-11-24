from django.conf.urls import url, include
from rest_framework import routers

from .views import CategoryViewSet, CategoryView, CategoryDetailView


router = routers.SimpleRouter(trailing_slash=False)
router.register('categories', CategoryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^category/(?P<pk>[0-9]+)$', CategoryDetailView.as_view()),
    url(r'^details/', CategoryView.as_view()),
]

