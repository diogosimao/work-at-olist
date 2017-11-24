from django.db import models

from neattree.core.models import DefaultBaseModel
from apps.categories.models import Category


class Channel(DefaultBaseModel):
    categories_m2m = models.ManyToManyField(Category, blank=True, related_name='categories_m2m',
                                            on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

