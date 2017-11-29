from django.db import transaction
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from apps.categories.models import Category
from apps.categories.views import tree_family_items_to_json
from apps.channels.models import Channel


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

    def test_default_category_view_with_valid_slug(self):
        """ Test default category view with valid slug"""

        sub_category = Category.objects.get(name='Sub Category')
        response = client.get(reverse('category:category_family', args=[sub_category.slug]))
        instances = sub_category.get_family()
        json_data = tree_family_items_to_json(instances)
        self.assertEqual(response.data, json_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_default_category_view_with_invalid_slug(self):
        """ Test default category view with invalid slug"""

        response = client.get(reverse('category:category_family', args=['wrong_slug']))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

