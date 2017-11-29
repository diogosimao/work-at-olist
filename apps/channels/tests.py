from django.db import transaction
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from .models import Channel
from .serializers import ChannelSerializer, ChannelCategoriesSerializer
from apps.categories.models import Category


class ChannelModelTest(TestCase):
    def test_string_representation(self):
        """ Test channel model string representation"""

        channel = Channel(name='Channel Name')
        self.assertEqual(str(channel), channel.name)

    def test_verbose_name_plural(self):
        """ Test channel model plural string representation"""

        self.assertEqual(str(Channel._meta.verbose_name_plural), "channels")


# initialize the APIClient app
client = Client()


class ChannelViewTest(TestCase):
    def setUp(self):
        channel = Channel(name='Channel Test1')
        channel.save()
        channel = Channel(name='Channel Test2')
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

    def test_get_all_channels(self):
        # get API response
        response = client.get(reverse('channel:channels_list'))
        # get data from db
        channels = Channel.objects.all()
        serializer = ChannelSerializer(channels, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_channel_categories(self):
        channel = Channel.objects.get(name='Channel Test2')
        response = client.get(reverse('channel:channels_categories', args=[channel.slug]))
        serializer = ChannelCategoriesSerializer(channel)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

