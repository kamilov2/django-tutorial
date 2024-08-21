from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView,DetailView
from django.views.generic.edit import DeleteView
from django.views import View
from .models import Movie,Comment,Rating,Category, Genre
from django.utils import timezone
from django.db.models import Count
from datetime import timedelta
from django.db.models import Q

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
    genres_selected = request.GET.getlist('genres[]')
    countries_selected = request.GET.getlist('countries[]')
    years_selected = request.GET.getlist('years[]')
    quality_selected = request.GET.getlist('quality[]')
    movies = Movie.objects.all()
    category = Category.objects.all()
    movie_context = []
    movie_context_ = []
    if genres_selected:
        movie = movies.filter(genres__slug__in=genres_selected).all()
        movie_context.append([i for i in movie])
        
    if countries_selected:
        movie = movies.filter(country__name__in=countries_selected).all()
        movie_context.append([i for i in movie])
        
    if years_selected:
        movie = movies.filter(year__in=years_selected).all()
        movie_context.append([i for i in movie])
    if quality_selected:
        movie = movies.filter(quality__in=quality_selected).all()
        movie_context.append([i for i in movie])
        
    for i in movie_context:
        for j in i:
            if j not in movie_context_:
                 movie_context_.append(j)
            
    
    geners = Genre.objects.all()
    context = {
               'object_list':movie_context_,
               'category':category,
               "genres":geners
               }
    print(movie_context_)
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


def movie_sort(request,key):
    today = timezone.now().date()
    yesterday = today - timedelta(days=1)
    movies = Movie.objects.all()
    category = Category.objects.all()
    context = {'object_list':movies,'category':category}
    
    if key == "year":
        movies = Movie.objects.order_by('-year')
        context = {'object_list':movies,'category':category}
        
    if key == "for_day":
        popular_movies = Movie.objects.annotate(
        num_comments=Count('comments', filter= Q(comments__created_at__date=today))
        ).filter(num_comments__gt=0).order_by('-num_comments')
        context = {'object_list':popular_movies,'category':category}
        
    if key == "for_week":
        one_week_before = today - timedelta(days=7)
        popular_movies = Movie.objects.annotate(
            num_comments=Count('comments', filter= Q(comments__created_at__date__lte=today,comments__created_at__date__gte = one_week_before))
        ).filter(num_comments__gt=0).order_by('-num_comments')
        context = {'object_list':popular_movies,'category':category}
        
    if key == "for_month":
        one_month_before = today - timedelta(days=31)
        popular_movies = Movie.objects.annotate(
            num_comments=Count('comments', filter= Q(comments__created_at__date__lte=today,comments__created_at__date__gte = one_month_before))
        ).filter(num_comments__gt=0).order_by('-num_comments')
        context = {'object_list':popular_movies,'category':category}
        
    if key == "for_all_time":
        popular_movies = Movie.objects.annotate(
            num_comments=Count('comments', filter= Q(comments__created_at__date__lte=today))
        ).filter(num_comments__gt=0).order_by('-num_comments')
        context = {'object_list':popular_movies,'category':category}
    
    if key == "for_user":
        popular_movies = Movie.objects.all().order_by('-rating_count')
        context = {'object_list':popular_movies,'category':category}
        
    if key == "for_kinobase":
        popular_movies = Movie.objects.all().order_by('-kp_rating')
        context = {'object_list':popular_movies,'category':category}
    
    if key == "for_imdb":
        popular_movies = Movie.objects.all().order_by('-imdb_rating')
        context = {'object_list':popular_movies,'category':category}
    
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
        
        

