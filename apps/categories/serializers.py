from rest_framework_recursive.fields import RecursiveField
from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    channel = serializers.ReadOnlyField(source='channel.slug')

    class Meta:
        model = Category
        fields = ('slug', 'name', 'channel')
        read_only_fields = ('slug', 'name', 'channel')


class CategoriesSerializer(serializers.ModelSerializer):
    subcategories = serializers.ListSerializer(source='children', child=RecursiveField(), required=False)
    channel = serializers.ReadOnlyField(source='channel.slug')

    class Meta:
        model = Category
        fields = ('slug', 'name', 'subcategories', 'channel')
        read_only_fields = ('slug', 'name', 'subcategories', 'channel')

