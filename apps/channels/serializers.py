from rest_framework import serializers

from .models import Channel
from apps.categories.serializers import CategorySerializer


class ChannelSerializer(serializers.ModelSerializer):
    categories_m2m = CategorySerializer(many=True)

    class Meta:
        model = Channel
        fields = ('slug', 'name', 'categories_m2m')
        read_only_fields = ('slug', 'created_at')

