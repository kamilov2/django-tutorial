from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="subcategories")

    def __str__(self):
        return self.name

COLOR_CHOICES = [
    ('red', 'Red'),
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('yellow', 'Yellow'),
    ('black', 'Black'),
    ('white', 'White'),
]
    
class Product(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="products")
    image = models.ImageField(upload_to="products/", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0) # 999999.99()
    colors = models.CharField(max_length=250, choices=COLOR_CHOICES,blank=True)
    cell_count = models.PositiveSmallIntegerField(default=0)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    rating_value = models.PositiveSmallIntegerField(default=0)
    discount = models.PositiveSmallIntegerField(default=0)
    stock = models.PositiveSmallIntegerField(default=0)
    avilable = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="ratings")
    value = models.PositiveSmallIntegerField(default=0)
    name = models.CharField(max_length=250, blank=True)
    comment = models.TextField(blank=True)
    
    def __str__(self):
        return self.product.name
    

class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products/", blank=True)
    
    def __str__(self):
        return self.product.name