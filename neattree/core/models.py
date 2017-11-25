from django.db import models
from autoslug import AutoSlugField

from .utils import generate_random_string


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-updated_at', '-created_at']


class DefaultBaseModel(TimestampedModel):
    slug = AutoSlugField(db_index=True, max_length=255, unique=True, populate_from='name',
                         slugify=generate_random_string)
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True
        ordering = ['slug', 'name']


