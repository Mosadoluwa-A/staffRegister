from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.urls import  reverse
from department.models import Department


def home(request):
    return render(request, 'users/home.html')


def home_msg(request, msg):
    return render(request, 'users/home.html', {'msg': msg})


def home_error(request, error):
    return render(request, 'users/home.html', {'error': error})


def login_user(request):
    user_model = get_user_model()
    user_log = user_model.objects.all()
    if request.method == "GET":
        return render(request, 'users/index.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        print("user is {}".format(user.username))
        if user is None:
            return render(request, {'error': 'Sorry username and passwords did not match'})
        else:
            login(request, user)
            print("session user{}".format(request.user))
            return redirect(reverse(home))


def register_user(request):
    departments = Department.objects.all()
    if request.method == "GET":
        return render(request, 'users/register.html', {'departments': departments})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user_model = get_user_model()
                username = request.POST['username']
                password = request.POST['password1']
                fname = request.POST['first_name']
                lname = request.POST['last_name']
                email = request.POST['email']
                department = request.POST['department']
                role = request.POST['role']
                image = request.POST['image']
                user = user_model.objects.create_user(username, password=password)
                user.first_name = fname
                user.last_name = lname
                user.email = email
                user.department = department
                user.role = role
                user.image = image
                user.save()
                login(request, user)
                return redirect(home)
            except IntegrityError:
                return render(request, 'users/register.html', {'error': 'The username has been taken please pick a different one'})
        else:
            return render(request, 'users/register.html', {'error': 'Sorry your passwords did not match'})


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect(login_user)

