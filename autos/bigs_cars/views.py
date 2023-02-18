from django.shortcuts import render, redirect
from .models import BigsCars
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def home(request):
    return render(request, 'bigs_cars/home.html')


def index(request):
    projects = BigsCars.objects.all()
    return render(request, 'bigs_cars/index.html', {'projects': projects})


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'bigs_cars/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'bigs_cars/signupuser.html', {
                    'form': UserCreationForm(),
                    'error': "Такое имя пользователя уже существует. Задайте другое."})

        else:
            return render(request, 'bigs_cars/signupuser.html', {
                'form': UserCreationForm(),
                'error': "Пароли не совпадают"})


def loginuser(request):     # вход (Авторизация)
    if request.method == 'GET':
        return render(request, 'bigs_cars/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'bigs_cars/loginuser.html', {'form': AuthenticationForm(),
                                                                'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('index')


def logoutuser(request):      # выход (разлогиниться)
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def currentautos(request):
    return render(request, 'bigs_cars/currentautos.html')

