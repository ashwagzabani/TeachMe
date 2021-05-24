# main_app/views.py
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', {"title": "Home"})


def log_in(request):
    return render(request, 'index.html', {"title": "Log In"})


def sign_up(request):
    return render(request, 'index.html', {"title": "Sign Up"})
