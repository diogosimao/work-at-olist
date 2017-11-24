from django.shortcuts import render
from rest_framework import viewsets, generics

from .models import Category
from .serializers import CategorySerializer


def index(request):
    return render(request, 'index.html',
                  {'nodes': Category.objects.all()})


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.root_nodes()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

