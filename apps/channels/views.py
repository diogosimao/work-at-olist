from rest_framework import generics

from .models import Channel
from .serializers import ChannelSerializer, ChannelCategoriesSerializer


class ChannelViewSet(generics.ListAPIView):
    lookup_field = 'slug'
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class ChannelCategoriesViewSet(generics.RetrieveAPIView):
    lookup_field = 'slug'
    queryset = Channel.objects.all()
    serializer_class = ChannelCategoriesSerializer

    def get_queryset(self):
        queryset = Channel.objects.all()
        slug = self.request.query_params.get('slug', None)
        if slug is not None:
            queryset = Channel.objects.filter(slug=slug)
        return queryset
