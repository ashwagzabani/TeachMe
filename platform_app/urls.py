# main_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logIn/', views.log_in, name='log_in'),
    path('signUp/', views.sign_up, name='sign_up'),
]
