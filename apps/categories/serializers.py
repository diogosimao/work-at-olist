from rest_framework_recursive.fields import RecursiveField
from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.ListSerializer(source='children',
                                               child=RecursiveField())

    class Meta:
        model = Category
        fields = ('slug', 'name', 'subcategories', 'channel')
        read_only_fields = ('slug', 'created_at', 'channel')

