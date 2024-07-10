from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug','category']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','subcategory','price','stock','created_at']
    list_filter = ['subcategory','price','created_at']
    list_editable = ['price','stock']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Rating)
admin.site.register(ProductImage)