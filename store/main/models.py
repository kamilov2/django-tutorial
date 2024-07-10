from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name
class SubCategory(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    def __str__(self):
        return self.name



class Brand(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

COLORS = [
    ('red', 'Red'),
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('yellow', 'Yellow'),
    ('black', 'Black'),
    ('white', 'White'),
]

class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=150, unique=True)
    image = models.ImageField(upload_to="product/images/", blank=True)
    price = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField("Discount %",default=0)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT, related_name="subcategory_products")
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="brand_products")
    colors = models.CharField(max_length=50, choices=COLORS, blank=True)
    cell_count = models.PositiveIntegerField("Cell Count",default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    rating_value = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    
    
    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="product/images/", blank=True)

    def __str__(self):
        return self.product.name

class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="ratings")
    value = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=150, blank=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.value
    