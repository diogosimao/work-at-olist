from django.db import transaction
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from apps.channels.models import Channel
from apps.channels.serializers import ChannelSerializer, ChannelCategoriesSerializer
from apps.categories.models import Category


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
        """ Test default channel view """
        # get API response
        response = client.get(reverse('channel:channels_list'))
        # get data from db
        channels = Channel.objects.all()
        serializer = ChannelSerializer(channels, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_channel_categories(self):
        """ Test all channel's categories view with valid slug """

        channel = Channel.objects.get(name='Channel Test2')
        response = client.get(reverse('channel:channels_categories', args=[channel.slug]))
        serializer = ChannelCategoriesSerializer(channel)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_all_channel_categories_view_with_invalid_slug(self):
        """ Test all channel's categories view with invalid slug """

        response = client.get(reverse('channel:channels_categories', args=['wrong_slug']))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

