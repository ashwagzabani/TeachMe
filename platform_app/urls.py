# main_app/urls.py
from django.urls import path
from django.views.generic.base import TemplateView
from . import views
from . import forms
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('logIn/', auth_views.LoginView.as_view(template_name='users/logIn.html'), name='logIn'),
    path('logOut/', views.logout_view, name='logOut'),
    path('register/', views.register, name='register'),
    path('course/create/', views.CourseDefinitionForm.as_view(template_name='courses/base_creation_form.html'),
         name='courseCreate'),
    # path('course/create/', views.courseCreate.as_view(template_name='courses/create.html'),
    #      name='courseCreate'),
    path('courses-list/', views.courses_list, name='courses_list'),
    path('category/', views.category_courses_list, name='category_courses_list'),
]
