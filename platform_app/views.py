# main_app/views.py
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def log_in(request):
    return render(request, 'index.html')


def sign_up(request):
    return render(request, 'index.html')
