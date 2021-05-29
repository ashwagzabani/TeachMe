from django.db import models

# Create your models here.
class Courses(models.Model):
    subject = models.CharField(max_length=250)
    category_name = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    age = models.IntegerField()

class Categories(models.Model):
    category_name = models.CharField(max_length=250)
