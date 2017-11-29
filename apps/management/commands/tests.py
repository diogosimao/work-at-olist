import os

from django.core.management import call_command
from django.test import TestCase


class CommandsTestCase(TestCase):
    def test_importcategories_command(self):
        """ Test importcategories custom command must return False."""

        args = ['channel_name', 'file_name.txt']
        opts = {}
        command_return = call_command('importcategories', *args, **opts)
        self.assertEqual(command_return, False)

    def test_importcategories_command(self):
        """ Test importcategories custom command must return None."""

        args = ['marketplace_test', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_data.txt')]
        opts = {}
        command_return = call_command('importcategories', *args, **opts)
        self.assertEqual(command_return, None)

