from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from neattree.core.models import DefaultBaseModel
from apps.channels.models import Channel


class Category(MPTTModel, DefaultBaseModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='children', db_index=True)
    channel = models.ForeignKey(Channel, related_name='categories', null=True, blank=True,)

    def __str__(self):
        return '{}'.format(self.name)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = "categories"

