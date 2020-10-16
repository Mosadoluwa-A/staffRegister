from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from department.models import Department
from .forms import RegisterForm
from .models import User



def home(request):
    name = request.session['name']
    if name:
        return render(request, 'users/home.html', {'name': name})
    else:
        return redirect(login_user)


def login_user(request):
    user = request.session['name']
    if request.method == "GET":
        return render(request, 'users/index.html', {'user': user})
    else:
        try:
            user = User.objects.get(username=request.POST['username'])
            if user and user.password == request.POST['password']:
                request.session['user_id'] = user.id
                request.session['name'] = user.name
                return redirect(home)
            else:
                return render(request, 'users/index.html', {'error': 'Invalid Login Details'})
        except ObjectDoesNotExist:
            return render(request, 'users/index.html', {'error': 'Invalid Login Details'})


def register_user(request):
    departments = Department.objects.all()
    if request.method == "GET":
        return render(request, 'users/register.html', {'departments': departments})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                userform = RegisterForm(request.POST)
                if userform.is_valid():
                    userform.save()
                return render(request, 'users/register.html', {'departments': departments, 'msg': 'User Successfully Created'})
            except IntegrityError:
                return render(request, 'users/register.html', {'error': 'The username has been taken please pick a different one'})
        else:
            return render(request, 'users/register.html', {'error': 'Sorry your passwords did not match'})


def logout_user(request):
    if request.method == "POST":
        try:
            del request.session['user_id']
            del request.session['user_id']
        except KeyError:
            pass
        return redirect(login_user)

