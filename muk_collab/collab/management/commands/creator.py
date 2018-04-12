import datetime, time

import schedule
from django.core.management import BaseCommand

from collab.models import *
from collab.team_creator import clear_booking


class Command(BaseCommand):

    help = 'collabo'

    def handle(self, *args, **options):

        schedule.every(1).minutes.do(clear_booking)
        # schedule.every().hour.do(clear_booking)

        while True:
            schedule.run_pending()
            time.sleep(1)
