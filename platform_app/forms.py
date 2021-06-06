from platform_app.models import User_profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    is_teacher = forms.BooleanField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'is_teacher', 'password1', 'password2']
