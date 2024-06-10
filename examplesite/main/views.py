import datetime
from django.shortcuts import render

from . models import Course,Group,Student

# Create your views here.
def home_page(request):
    data = {
        # objects - Django ORM  baza bilan ishlash
        "courses":Course.objects.all(), # SELECT * FROM course
        "groups":Group.objects.all(),
    }
    # print(dir(Course.objects.all()))
    return render(request, "index.html", context=data)

def course_detail(request,course_id):
    context = {
        "object":Course.objects.get(id=course_id)
    }
    return render(request, "course-detail.html", context)