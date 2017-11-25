from rest_framework import serializers

from .models import Channel
from apps.categories.serializers import CategorySerializer


class ChannelSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Channel
        fields = ('slug', 'name', 'categories')
        read_only_fields = ('slug', 'created_at')

