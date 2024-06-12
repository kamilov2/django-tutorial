from django.contrib import admin
from .models import Category,Tag,Post
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","id","slug"]
    prepopulated_fields = {"slug":("name",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name","id","slug"]
    prepopulated_fields = {"slug":("name",)}
    
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title","id","slug"]
    prepopulated_fields = {"slug":("title",)}
    
