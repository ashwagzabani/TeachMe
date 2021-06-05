from .models import Courses, Categories


def categories(request):
    categoriesList = Categories.objects.all()
    return {"categories": categoriesList}
