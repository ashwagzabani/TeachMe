from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class User_profile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to='profile_img/', blank=True, default='profile_img/profile.png', verbose_name="Picture:")
    is_teacher = models.BooleanField(default=False)


class Categories(models.Model):
    category_name = models.CharField(max_length=250)


class Courses(models.Model):
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    age = models.IntegerField()
    course_image = models.ImageField(
        upload_to='profile_img/', blank=True, default='profile_img/profile.png', verbose_name="Picture:")
    requirment = models.CharField(max_length=250)
    language = models.CharField(max_length=250)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    rate = models.FloatField()
    is_private = models.BooleanField(default=False)


class Enrollment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
