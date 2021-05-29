from django.contrib import admin
from .models import Courses
from .models import Categories

# Register your models here
admin.site.register(Courses)
admin.site.register(Categories)
