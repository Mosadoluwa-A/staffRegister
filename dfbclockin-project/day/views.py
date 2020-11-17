from django.shortcuts import render
from .models import Day


def all_days(request):
    days = Day.objects.all()
    return render(request, 'day/days.html', {'days': days})


