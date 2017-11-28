from django.test import TestCase

from .models import Channel


class ChannelModelTest(TestCase):
    def test_string_representation(self):
        """ Test channel model string representation"""

        channel = Channel(name='Channel Name')
        self.assertEqual(str(channel), channel.name)

    def test_verbose_name_plural(self):
        """ Test channel model plural string representation"""

        self.assertEqual(str(Channel._meta.verbose_name_plural), "channels")