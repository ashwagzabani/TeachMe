# main_app/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Courses


def index(request):
    courses = Courses.objects.all()
    return render(request, 'index.html', {"title": "Home", "courses": courses})


def log_in(request):
    return render(request, 'index.html', {"title": "Log In"})


def sign_up(request):
    return render(request, 'index.html', {"title": "Sign Up"})


def courses_list(request):
    return render(request, 'courses_list.html', {"title": "courses list"})
