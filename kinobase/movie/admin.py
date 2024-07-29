from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","slug"]
    prepopulated_fields = {"slug":("name",)}
    
    
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["id","slug"]
    prepopulated_fields = {"slug":("name",)}
    
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["id","slug"]
    prepopulated_fields = {"slug":("title",)}


admin.site.register(Role)
admin.site.register(Rating)
admin.site.register(Author)
admin.site.register(Comment)