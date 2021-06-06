# main_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logIn/', views.log_in, name='log_in'),
    path('register/', views.register, name='register'),
    path('courses-list/', views.courses_list, name='courses_list'),
    path('category/', views.category_courses_list, name='category_courses_list'),
]
