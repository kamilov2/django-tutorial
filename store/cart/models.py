from django.db import models
from main.models import Product
# Create your models here.

class CartProducts(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return self.product.name

class Cart(models.Model):
    products = models.ManyToManyField(CartProducts)
    total_quantity = models.PositiveSmallIntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return f"Cart id = {self.id}"
    
    
    def add(self, product_id, qty=1):
        product = Product.objects.get(id=int(product_id))
        price = product.get_discount_price() * qty
        self.products.add(product=product, quantity=int(qty), price=price)
        return True