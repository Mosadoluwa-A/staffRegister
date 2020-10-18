from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import ClockinForm
from users.views import home_msg, home_error


# def clock_in(request):
#     if request.method == "POST":
#         try:
#             form = ClockinForm(request.POST)
#             newclockin = form.save(commit=False)
#             newclockin.user = request.user
#             newclockin.save()
#             return redirect(home_msg, msg="You have successfully clocked in!")
#         except ValueError:
#             return redirect(home_error, error=request.user)

def clock_in(request):
    if request.method == "POST":
        form = ClockinForm(request.POST)
        newclockin = form.save(commit=False)
        print("USER: {}".format(request.user))
        newclockin.user = request.user
        newclockin.save()
    return redirect(home_msg, msg="You have successfully clocked in!")





