from rest_framework_recursive.fields import RecursiveField
from rest_framework import serializers

from .models import Category


class CategoriesSerializer(serializers.ModelSerializer):
    subcategories = serializers.ListSerializer(source='get_children', child=RecursiveField(), required=False)

    class Meta:
        model = Category
        fields = ('slug', 'name', 'subcategories', 'channel')
        read_only_fields = ('slug', 'name', 'subcategories', 'channel')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('slug', 'name', 'channel')
        read_only_fields = ('slug', 'name', 'channel')

