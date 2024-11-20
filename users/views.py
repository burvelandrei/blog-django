from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import DetailView
from .models import CustomUser
from .forms import RegistrationForm, LoginForm


class profile(DetailView):
    model = CustomUser
    template_name = "users/profile.html"


def register(request):
    if request.method == 'GET':
        registration_form = RegistrationForm()
        return render(request, 'users/register.html', {'form': registration_form})
    elif request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save()
            login(request, user)
            return redirect('index')
        else:
            # Если форма невалидна, передаем ее обратно в шаблон с ошибками
            return render(request, 'users/register.html', {'form': registration_form})
    else:
        registration_form = RegistrationForm()
    return render(request, 'users/register.html', {'form': registration_form})

def user_login(request):
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'users/login.html', {'form': login_form})
    elif request.method == 'POST':
        login_form = LoginForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        login_form = LoginForm()
    return render(request, 'users/login.html', {'form': login_form})

def user_logout(request):
    if request.method == 'GET':
        logout(request)
        return redirect('index')