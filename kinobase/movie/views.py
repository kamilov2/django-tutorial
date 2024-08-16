from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView,DetailView
from django.views.generic.edit import DeleteView
from django.views import View
from .models import Movie,Comment,Rating,Category, Genre
# Create your views here.

class MovieListView(ListView):
    model = Movie
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['geners'] = Genre.objects.all()
        return context


def category(request,slug):
    movies = Movie.objects.filter(category__slug=slug)
    category = Category.objects.all()
    one_category = Category.objects.get(slug = slug)
    geners = Genre.objects.all()
    context = {
                'object_list':movies,
               'category':category, 
               "one_category":one_category,
               "genres":geners
        }
    return render(request,'index.html', context)


def genre_filter(request):
    selected_options = request.GET.getlist('options')
    category = Category.objects.all()
    movies = []
    for i in selected_options:
        genre = Genre.objects.get(slug = i)
        mouvi = genre.mouvies.all()
        for i in mouvi:
            movies.append(i)
    geners = Genre.objects.all()
    context = {
                'object_list':movies,
               'category':category,
               "genres":geners
               }

    return render(request,'index.html', context)


def search(request):
    context = {}
    movies = Movie.objects.filter(origin_title__icontains=request.GET.get("query"))
    if movies:
        context["object_list"] = movies
    else:
        movies = Movie.objects.filter(title__icontains=request.GET.get("query"))
    category = Category.objects.all()
    context = {'object_list':movies,'category':category}
    return render(request,'index.html', context)


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movie_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(movie=self.object)
        context['comments'] = comments
        context['rating'] = Rating.objects.filter(movie=self.object)
        return context

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            movie = self.get_object()
            user = request.user
            text = request.POST.get("comment")
            Comment.objects.create(movie=movie,user=user,text=text)
            messages.success(request, "Комментарий добавлен !")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return redirect(reverse('users:login'))

def comment_delete(request,comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    messages.success(request, "Комментарий удален !")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def set_rating(request, rating_value,movie_id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(id=movie_id)
        Rating.objects.create(movie=movie, user=request.user, value=rating_value)
        movie.rating_count += 1
        movie.save()
    else:
        return redirect(reverse('users:login'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def add_favorite(request, movie_id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(id=movie_id)
        profile = request.user.profile
        if profile.favorites.filter(id=movie_id).exists():
            profile.favorites.remove(movie)
            messages.info(request, "Фильм удален из избранного !")
        else:
            profile.favorites.add(movie)
            messages.success(request, "Фильм добавлен в избранное !")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(reverse('users:login'))
    
def favourites_page(request):
    if request.user.is_authenticated:
        profile = request.user.profile
        return render(request, 'collections.html', {'favourites': profile.favorites.all()})
    else:
        return redirect(reverse('users:login'))
        
        

