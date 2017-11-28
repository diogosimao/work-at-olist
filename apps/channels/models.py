from django.db import models

from neattree.core.models import DefaultBaseModel


class Channel(DefaultBaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = "channels"

