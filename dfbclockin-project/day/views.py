from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Day
from datetime import datetime, date
from users.models import User
from .forms import AbsentForm
from users.views import home, home_error


@login_required(login_url='/')
def all_days(request):
    role = request.session['role']
    if role == 'administrator':
        days = Day.objects.all().order_by('-created')
        admin = request.session['role']
        return render(request, 'day/days.html', {'days': days, 'admin': admin})
    else:
        messages.error(request, "You do not have permission to view the page")
        return redirect(home)


@login_required(login_url='/')
def attendance(request, day_id):
    role = request.session['role']
    if role == 'administrator':
        day = get_object_or_404(Day, pk=day_id)
        clocks = day.clockins.all()
        admin = request.session['role']
        return render(request, 'day/attendance.html', {'day': day, 'clocks': clocks, 'admin': admin})
    else:
        messages.error(request, "You do not have permission to view the page")
        return redirect(home)


@login_required(login_url='/')
def absent_days(request):
    role = request.session['role']
    if role == 'administrator':
        days = Day.objects.all().order_by('-created')
        admin = request.session['role']
        return render(request, 'day/absent_days.html', {'days': days, 'admin': admin})
    else:
        messages.error(request, "You do not have permission to view the page")
        return redirect(home)


@login_required(login_url='/')
def absentees(request, day_id):
    role = request.session['role']
    if role == 'administrator':
        day = get_object_or_404(Day, pk=day_id)
        absents = day.absents.all()
        admin = request.session['role']
        return render(request, 'day/absent_detail.html', {'day': day, 'absents': absents, 'admin': admin})
    else:
        messages.error(request, "You do not have permission to view the page")
        return redirect(home)


@login_required(login_url='/')
def add_absent_staff(request):
    role = request.session['role']
    if role == 'administrator':
        today = date.today().strftime("%d, %B %Y")
        get_day = Day.objects.filter(name=today).first()
        if request.method == "POST" and get_day is not None:
            try:
                form = AbsentForm(request.POST)
                newabsentee = form.save(commit=False)
                newabsentee.day = get_day
                newabsentee.save()
                return redirect(absent_days)
            except ValueError:
                messages.error(request, "form did not submit " + request.POST['staff'])
                return redirect(add_absent_staff)

        elif request.method == "GET":
            users = User.objects.all()
            admin = request.session['role']
            return render(request, 'day/absent_form.html', {'users': users, 'admin': admin})
    else:
        messages.error(request, "You do not have permission to view the page")
        return redirect(home)

    return redirect(home_error, error="No Day Created")


