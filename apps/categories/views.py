import json

from django.shortcuts import render
from mptt.utils import tree_item_iterator
from rest_framework import generics
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer


def index(request):
    return render(request, 'index.html',
                  {'nodes': Category.objects.all()})


class CategoryFamily(generics.RetrieveAPIView):
    lookup_field = 'slug'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object().get_family()
        data = ''
        for category, structure in tree_item_iterator(instance):
            if structure['new_level']:
                data += '{'
            else:
                data += '],'
                data += '"channel": {}'.format(category.channel.id)
                data += '},{'
            data += '"slug": "{}",'.format(category.slug)
            data += '"name": "{}",'.format(category.name)
            data += '"subcategories": ['
            for level in structure['closed_levels']:
                data += '],'
                data += '"channel": {}'.format(category.channel.id)
                data += '}'

        return Response(json.loads(data))

