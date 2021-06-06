# main_app/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm


def index(request):
    courses = Courses.objects.all()
    return render(request, 'index.html', {"title": "Home", "courses": courses})


def log_in(request):
    return render(request, 'index.html', {"title": "Log In"})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # to save data to db
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created successfully for {username} .')
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {"form": form})


def courses_list(request):
    return render(request, 'courses_list.html', {"title": "courses list"})


def category_courses_list(request):
    courses = Courses.objects.all()
    return render(request, 'category_courses_list.html', {"category": courses})
