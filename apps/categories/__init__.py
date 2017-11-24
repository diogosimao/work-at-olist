from django.apps import AppConfig


class CategoriesAppConfig(AppConfig):
    name = 'apps.categories'
    label = 'categories'
    verbose_name = 'Categories'


default_app_config = 'apps.categories.CategoriesAppConfig'

