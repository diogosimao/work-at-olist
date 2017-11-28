from rest_framework import generics
from rest_framework.response import Response

from .models import Channel
from .serializers import ChannelSerializer, ChannelCategoriesSerializer


class ChannelView(generics.ListAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class ChannelCategoriesView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    queryset = Channel.objects.all()
    serializer_class = ChannelCategoriesSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

