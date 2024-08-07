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
    
admin.site.register(Role)

class MovieRoleStackedInline(admin.StackedInline):
    model = Role
    extra = 3
    
    
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["id", "title",]
    prepopulated_fields = {"slug":("title",)}
    inlines = [MovieRoleStackedInline]




@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id","slug"]
    prepopulated_fields = {"slug":("name",)}

admin.site.register(Rating)
admin.site.register(Comment)