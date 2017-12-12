import os

from django.core.management.base import BaseCommand
from django.db import transaction, DatabaseError

from apps.categories.models import Category
from apps.channels.models import Channel


def get_channel(channel_name):
    obj = Channel.objects.filter(name__iexact=channel_name).first()
    if obj is not None:
        return obj
    obj = Channel(name=channel_name)
    obj.save()
    return obj


def import_categories(categories_dict, channel=None, parent=None):
    with transaction.atomic():
        with Category.objects.disable_mptt_updates():
            for key, value in categories_dict.items():
                new_category = Category(name=key, channel=channel, parent=parent)
                new_category.save()
                import_categories(value, parent=new_category)
        Category.objects.rebuild()


def full_update(channel):
    with transaction.atomic():
        categories = Category.objects.root_nodes()
        categories = categories.filter(channel=channel)
        categories.delete()


def read_file_lines(file_path):
    with open(file_path, 'r') as file:
        file_lines = file.readlines()
        return file_lines


def create_dict_tree(main_dict, array):
    if len(array) == 0:
        return
    item = array[0].rstrip().lstrip()
    if not item:
        return
    if item not in main_dict.keys():
        main_dict[item] = {}
    create_dict_tree(main_dict[item], array[1:])


def parser_categories_file(file_path):
    lines = read_file_lines(file_path)
    main_dict = {}
    for line in lines:
        array = line.split('/')
        root = array[0].rstrip().lstrip()
        if not root:
            continue
        if root not in main_dict.keys():
            main_dict[root] = {}
        if len(array[1:]) == 0:
            continue

        create_dict_tree(main_dict[root], array[1:])

    return main_dict


class Command(BaseCommand):
    help = 'A Django Management Command to import the channels\' categories from a text file.'

    def add_arguments(self, parser):
        parser.add_argument('channel_name', type=str,
                            help='Channel name (create the channel if it doesn\'t exists in database)')
        parser.add_argument('file_name', type=str,
                            help='The name of .txt file with the full category\'s path')

    def handle(self, *args, **options):

        file_path = os.path.join(os.path.curdir, options['file_name'])
        if not os.path.exists(file_path):
            if os.path.isabs(options['file_name']):
                file_path = options['file_name']
            else:
                file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), options['file_name'])

            if not os.path.exists(file_path):
                self.stdout.write(self.style.ERROR("File not found"))
                return False

        try:
            main_dict = parser_categories_file(file_path=file_path)
        except:
            self.stdout.write(self.style.ERROR("Parser error"))
            return False

        try:
            channel = get_channel(options['channel_name'])
        except DatabaseError:
            self.stdout.write(self.style.ERROR("Channel error"))
            return False

        try:
            full_update(channel)
            import_categories(main_dict, channel=channel)
        except DatabaseError:
            self.stdout.write(self.style.ERROR("Import error"))
            return False

        self.stdout.write(self.style.SUCCESS('Success'))

