from django.core.management.base import BaseCommand, CommandError
from app.models import *


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        try:
            models = [GroupUsers(name='customer_group'), GroupUsers(
                name='store_group'), GroupUsers(name='owner_group')]
            GroupUsers.objects.bulk_create(models)
        except Exception, e:
            print 'Command ', e
            raise CommandError('Exception "%s" does not exist' % e)
