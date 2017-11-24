import random
import string

from django.utils.text import slugify


DEFAULT_CHAR_STRING = string.ascii_lowercase + string.digits
MAXIMUM_SLUG_LENGTH = 255
SIZE = 6


def generate_random_string(value):
    unique = ''.join(random.choice(DEFAULT_CHAR_STRING) for _ in range(SIZE))
    slug = slugify(value)

    if len(slug) > MAXIMUM_SLUG_LENGTH:
        slug = slug[:MAXIMUM_SLUG_LENGTH]

    while len(slug + '-' + unique) > MAXIMUM_SLUG_LENGTH:
        parts = slug.split('-')
        if len(parts) is 1:
            slug = slug[:MAXIMUM_SLUG_LENGTH - len(unique) - 1]
        else:
            slug = '-'.join(parts[:-1])

    return slug + '-' + unique

