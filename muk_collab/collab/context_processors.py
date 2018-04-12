import datetime


def years_processor(request):
    year = datetime.date.today().year
    return {'year':year}


def current_date_processor(request):
    current_date = datetime.date.today()
    return {'current_date':current_date}