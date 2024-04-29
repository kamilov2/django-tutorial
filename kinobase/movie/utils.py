import datetime
from .models import Movie,Genre

def get_movie_filter_years():
    # years = []
    # for movie in  Movie.objects.all():
    #     years.append(movie.year)
    # print()
    # years = list(set(years))
    # years.sort(reverse=True)
    years = []
    current_year = datetime.datetime.now().year
    for year in range(current_year-50,current_year+1):
        years.append(year)
    years.sort(reverse=True)
    return years

def get_country_list():
    countries = []
    for movie in Movie.objects.all():
        for c in movie.country:
            countries.append(c.name)
    countries = list(set(countries))

    countries.sort()
    return countries

def custom_context_proccessor(request):
    context = {
        "genres":Genre.objects.all(),
        "years":get_movie_filter_years(),
        "countries":get_country_list(),
    }
    return context
    