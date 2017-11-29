from django.conf.urls import url

from .views import CategoryFamily


urlpatterns = [
    url(r'^category/(?P<slug>[^/.]+)$', CategoryFamily.as_view(), name='category_family'),
]

