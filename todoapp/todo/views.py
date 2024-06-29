from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView ,UpdateView
# Create your views here.
from .models import Todo


class HomePageView(ListView):
    model = Todo
    template_name = "index.html"

    


class AddTodoView(CreateView):
    model = Todo
    # template_name = "index.html"
    fields = "__all__"
    success_url = "/"


    
class UpdateToDo(UpdateView):
    model = Todo
    # template_name = "index.html"
    fields = "__all__"
    success_url = "/"
