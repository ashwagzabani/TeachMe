from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    is_staff = forms.BooleanField(
        label='Register as instructor', required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2', 'is_staff']


# ------------------    form wizard ----------------------------------
# form 1: Course Definition
# class CourseDefinitionForm(ModelForm):
#     subject = forms.CharField(
#         label='Course subject')
#     category_id = forms.SelectMultiple()
#     course_image = forms.ImageField(
#         label='Cover image')

#     class Meta:
#         model = Courses
#         fields = ['subject', 'category_id', 'course_image']
#         labels = {'category_id': 'Course category'}
