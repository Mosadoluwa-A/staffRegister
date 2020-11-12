from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import ClockinForm
from users.views import home_msg, home_error
from .models import Clockin
from day.models import Day


def clock_in(request):
    # today = date.today().strftime('%d, %B %Y ')
    today = date.today().strftime("%d, %B %Y")
    get_day = Day.objects.filter(name=today).first()
    if request.method == "POST" and get_day is not None:
        try:
            form = ClockinForm(request.POST)
            newclockin = form.save(commit=False)
            newclockin.user = request.user
            print(get_day)
            newclockin.day = get_day
            newclockin.save()
            request.session['clockin_id'] = newclockin.id
            return redirect(home_msg, msg="You have successfully clocked in!")
        except ValueError:
            return redirect(home_error, error="Bad data passed in")
    else:
        print(get_day)
        return redirect(home_error, error="No Day Created")


def clock_out(request):
    clock_in_id = request.session['clockin_id']
    clocks_out = get_object_or_404(Clockin, pk=clock_in_id, user=request.user)
    if clock_in_id and request.method == "POST":
        clocks_out.time_out = timezone.now()
        clocks_out.save()
        return redirect(home_msg, msg="You have successfully clocked out!")

# def clock_in(request):
#     if request.method == "POST":
#         form = ClockinForm(request.POST)
#         newclockin = form.save(commit=False)
#         print("USER: {}".format(request.user))
#         newclockin.user = request.user
#         newclockin.save()
#     return redirect(home_msg, msg="You have successfully clocked in!")





