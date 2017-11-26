from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'A Django Management Command to import the channels\' categories from a text file.'

    def add_arguments(self, parser):
        parser.add_argument('channel_name', nargs='+', type=str,
                            help='Channel name (create the channel if it doesn\'t exists in database)')
        parser.add_argument('file_name', nargs='+', type=str,
                            help='The name of .txt file with the full category\'s path')

    def handle(self, *args, **options):
        try:
            pass
        except:
            raise CommandError('Error')

        self.stdout.write(self.style.SUCCESS('Success'))

