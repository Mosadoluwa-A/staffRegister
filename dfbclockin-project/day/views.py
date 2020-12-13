from django.shortcuts import render, get_object_or_404
from .models import Day


def all_days(request):
    days = Day.objects.all()
    admin = request.session['role']
    return render(request, 'day/days.html', {'days': days, 'admin':admin})


def attendance(request, day_id):
    day = get_object_or_404(Day, pk=day_id)
    clocks = day.clockins.all()
    admin = request.session['role']
    return render(request, 'day/attendance.html', {'day': day, 'clocks': clocks, 'admin': admin})


