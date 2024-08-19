from .models import Movie
from django.db.models import Q

def countries(request):
    countries = []
    year = []
    quality = []
    movies = Movie.objects.all()
    for i in movies:
        print(i.country)
        for j in i.country:
            if j not in countries:
                countries.append(j)
        if i.year not in year:
            year.append(i.year)
        if i.quality not in quality:
            quality.append(i.quality)
    context = {
        "countries" : countries,
        "years": year,
        "quality": quality,
    }
    return context
    