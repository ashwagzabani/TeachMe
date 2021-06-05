from django.contrib import admin
from .models import User_profile
from .models import Categories
from .models import Courses
from .models import Enrollment

# Register your models here
admin.site.register(User_profile)
admin.site.register(Categories)
admin.site.register(Courses)
admin.site.register(Enrollment)
