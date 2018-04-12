import datetime
import re

from django.core.management import BaseCommand

from collab.models import Project


class Command(BaseCommand):

    help = 'collabo'

    def handle(self, *args, **options):
        class Command(BaseCommand):
            help = 'collabo'
            x = ['1:00:00']
            z = re.findall(r'\d+', str(x))
            y = z[0]
            print int(y)