from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib import messages
from django.urls import reverse
from blog.models import Post, Comment

from .utils import check_reaction


def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "blog/detail.html", context)

class PostAddView(CreateView):
    model = Post
    # template_name = 
    fields = ['title','categories','body']
    success_message = 'Success !'
    
    
    def form_valid(self, form):
        # form.instance.save()
        # self.user.teams.add(form.instance)
        f = form.save(commit=False)
        f.author = self.request.user
        f.save()
        messages.add_message(self.request,messages.SUCCESS,'Success !')
        return super().form_valid(form)
    
    
    def get_success_url(self):
        return reverse('users:profile',kwargs={'pk':self.request.user.profile.id})
    
class PostDeleteView(DeleteView):
    model = Post
    
    
    def get_success_url(self):
        return reverse('users:profile',kwargs={'pk':self.request.user.profile.id})
    
class PostEditView(UpdateView):
    model = Post
    fields = ['title','categories','body']
    
    
    def get_success_url(self):
        return reverse('users:profile',kwargs={'pk':self.request.user.profile.id})
    



def set_reaction(request, post_id,action):
    post = Post.objects.get(id=post_id)
    status = check_reaction(request,post,action)
    messages.info(request, status)
    return redirect(request.META.get('HTTP_REFERER'))