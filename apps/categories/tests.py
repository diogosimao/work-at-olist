from django.db import transaction
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from .models import Category
from .views import tree_family_items_to_json
from apps.channels.models import Channel


class CategoryModelTest(TestCase):
    def setUp(self):
        with transaction.atomic():
            with Category.objects.disable_mptt_updates():
                parent_category = Category(name='Parent Category')
                parent_category.save()
                children_category = Category(name='Children Category', parent=parent_category)
                children_category.save()
            Category.objects.rebuild()

    def test_string_representation(self):
        """ Test category model string representation"""

        category = Category(name='Marketplace')
        self.assertEqual(str(category), category.name)

    def test_verbose_name_plural(self):
        """ Test category model plural string representation"""

        self.assertEqual(str(Category._meta.verbose_name_plural), "categories")

    def test_children_category(self):
        """ Test category children"""
        parent_category = Category.objects.get(name='Parent Category')
        children_category = Category.objects.get(name='Children Category')
        self.assertEqual(parent_category.get_children()[0].name, children_category.name)

    def test_parent_category(self):
        """ Test category parent"""
        parent_category = Category.objects.get(name='Parent Category')
        children_category = Category.objects.get(name='Children Category')
        self.assertEqual(children_category.parent.name, parent_category.name)


# initialize the APIClient app
client = Client()


class CategoryViewTest(TestCase):
    def setUp(self):
        channel = Channel(name='Channel Test')
        channel.save()

        with transaction.atomic():
            with Category.objects.disable_mptt_updates():
                parent_category = Category(name='Parent Category', channel=channel)
                parent_category.save()
                children_category = Category(name='Children Category', parent=parent_category, channel=channel)
                children_category.save()
                sub_category = Category(name='Sub Category', parent=children_category, channel=channel)
                sub_category.save()

            Category.objects.rebuild()

    def test_default_category_view(self):
        """ Test default category view"""

        sub_category = Category.objects.get(name='Sub Category')
        response = client.get(reverse('category:category_family', args=[sub_category.slug]))
        instances = sub_category.get_family()
        json_data = tree_family_items_to_json(instances)
        self.assertEqual(response.data, json_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


