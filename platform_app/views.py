# main_app/views.py
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic.edit import CreateView
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import User
from django.contrib import messages
from .forms import SignUpForm, CourseDefinitionForm


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
        form = SignUpForm()
    return render(request, 'users/register.html', {"form": form})


def logout_view(request):
    logout(request)
    messages.success(
        request, f'You are Logged out .')
    return HttpResponseRedirect('/')


def courses_list(request):
    return render(request, 'courses_list.html', {"title": "courses list"})


def category_courses_list(request):
    courses = Courses.objects.all()
    return render(request, 'category_courses_list.html', {"category": courses})


class CourseDefinitionForm(CreateView):
    model = Courses
    fields = ['subject', 'category_id', 'course_image']
    success_url = '/'

    def form_valid(self, form, *kwargs):
        self.object = form.save(commit=False)
        self.object.instroctor = self.request.user.id
        # self.object.save()
        return HttpResponseRedirect('/')


# class CourseDefinitionForm(CreateView):
#     subject = models.CharField(
#         label='Course subject')
#     category_id = models.SelectMultiple()
#     course_image = models.ImageField(
#         label='Cover image')

#     class Meta:
#         model = Courses

#     def __init__(*args, **kwargs):
#         super().__init__(*args, **kwargs)


# def courseDefinition(request):
#     if request.method == 'POST':
#         form = CourseDefinitionForm(request.POST)
#         if form.is_valid():
#             form.save()  # to save data to db
#             messages.success(
#                 request, f'Account created successfully for.')
#             return redirect('index')
#     else:
#         form = CourseDefinitionForm()
#     return render(request, 'users/register.html', {"form": form})
