from django.apps import AppConfig


class DayConfig(AppConfig):
    name = 'day'

    def ready(self):
        from .models import Day
        from datetime import date
        today = date.today().strftime("%d, %B %Y")
        month = date.today().strftime("%B")
        year = date.today().strftime("%Y")
        # print(today)
        # print(Day.objects.filter(name=today).first())
        check_today = Day.objects.filter(name=today).first()
        if check_today is not None:
            print("Today Exists")
        else:
            Day.objects.create(name=today, month=month, year=year)
            print('New day just created')

