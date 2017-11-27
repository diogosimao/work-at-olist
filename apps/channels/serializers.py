from rest_framework import serializers

from .models import Channel
from apps.categories.serializers import CategoriesSerializer


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('slug', 'name')
        read_only_fields = ('slug', 'name')


class ChannelCategoriesSerializer(serializers.ModelSerializer):
    categories = CategoriesSerializer(many=True, required=False)

    class Meta:
        model = Channel
        fields = ('slug', 'name', 'categories')
        read_only_fields = ('slug', 'name', 'categories')

