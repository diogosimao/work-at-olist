from django.db import transaction
from django.test import TestCase

from apps.categories.models import Category


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

