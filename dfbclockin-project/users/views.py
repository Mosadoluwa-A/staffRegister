from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.urls import reverse
from department.models import Department
from clockin.models import Clockin

# CLOCKIN


def home(request):
    User = get_user_model()
    name = request.session['name']
    role = request.session['role']
    user_id = request.session['user_id']
    if role == 'administrator':
        users = User.objects.all()
        admin = request.session['role']
        return render(request, 'users/admin.html', {'users': users, 'admin': admin, 'name': name, 'user_id': user_id})
    return render(request, 'users/home.html', {'name': name, 'role': role, 'user_id': user_id})


def admin_clockin(request):
    name = request.session['name']
    role = request.session['role']
    admin = request.session['role']
    if role == 'administrator':
        return render(request, 'users/home.html', {'name': name, 'role': role, 'admin': admin})


def user_clockins(request, user_id):
    User = get_user_model()
    user = get_object_or_404(User, pk=user_id)
    name = user.get_full_name()
    role = request.session['role']
    clockin = Clockin.objects.filter(user=user_id).order_by('created')
    if role == 'administrator':
        admin = request.session['role']
        return render(request, 'users/staffdashboard.html', {'clockins': clockin, 'name': name, 'admin': admin, 'user_id': user_id})
    return render(request, 'users/staffdashboard.html', {'clockins': clockin, 'name': name, 'user_id': user_id})


def home_msg(request, msg):
    return render(request, 'users/home.html', {'msg': msg})


def home_error(request, error):
    return render(request, 'users/home.html', {'error': error})


# AUTHENTICATION
def login_user(request):
    # user_model = get_user_model()
    if request.method == "GET":
        return render(request, 'users/index.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        print("user is {}".format(user.username))
        if user is None:
            return render(request, {'error': 'Sorry username and passwords did not match'})
        else:
            login(request, user)
            request.session['name'] = user.get_full_name()
            request.session['user_id'] = user.id
            request.session['role'] = user.role
            print("session user{}".format(request.user))
            print("session user id is {}".format(request.session['user_id']))
            print("session user department is {}".format(user.department))
            return redirect(reverse(home))


def register_user(request):
    departments = Department.objects.all()
    if request.method == "GET":
        return render(request, 'users/register.html', {'departments': departments})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user_model = get_user_model()
                files = request.FILES
                image = files.get("image")
                username = request.POST['username']
                password = request.POST['password1']
                fname = request.POST['first_name']
                lname = request.POST['last_name']
                email = request.POST['email']
                department = request.POST['department']
                role = request.POST['role']
                user = user_model.objects.create_user(username, password=password)
                user.first_name = fname
                user.last_name = lname
                user.email = email
                user.department = department
                user.role = role
                user.image = image
                user.save()
                login(request, user)
                request.session['name'] = user.get_full_name()
                request.session['id'] = user.id
                request.session['role'] = user.role
                return redirect(home)
            except IntegrityError:
                return render(request, 'users/register.html',
                              {'error': 'The username has been taken please pick a different one'})
        else:
            return render(request, 'users/register.html', {'error': 'Sorry your passwords did not match'})


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect(login_user)
