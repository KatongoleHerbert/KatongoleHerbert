import datetime
from collab.models import *


def clear_booking():
    Project.objects.filter(date=datetime.date.today(), end_time=datetime.datetime.now()).update(status=True)