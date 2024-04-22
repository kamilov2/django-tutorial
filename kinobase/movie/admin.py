from django.contrib import admin
from . models import *
# Register your models here.


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Genre)

class MovieRoleStackedInline(admin.StackedInline):
    model = Roles
    # fields = "__all__"
    
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {"slug":("name",)}
    inlines = [MovieRoleStackedInline]



    
