from django.apps import AppConfig


class ChannelsAppConfig(AppConfig):
    name = 'apps.channels'
    label = 'channels'
    verbose_name = 'Channels'


default_app_config = 'apps.channels.ChannelsAppConfig'

