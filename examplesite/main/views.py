import datetime
from django.shortcuts import render

# Create your views here.
def home_page(request):
    data = {
        "sitename":"examplesite",
        "frontent":"html and css",
        "backend":"Python Django",
        "now":datetime.datetime.now()
    }
    return render(request, "index.html", context=data)