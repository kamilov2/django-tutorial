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
    
    
    def add(self, product_id):
        product = Product.objects.get(id=product_id)
        self.products.create(
                product=product,
                quantity=1,
                price=product.get_discount_price()
            )
        self.total_quantity += 1
        self.total_price += product.get_discount_price()
        self.save()
        return True

    def cart_product_update(self,action,product_id,item_id):
        product = Product.objects.get(id=product_id)
        obj = self.products.get(id=item_id) 
        if action == "plus":
            self.total_price += obj.product.get_discount_price()
            self.total_quantity += 1
            obj.quantity += 1
            obj.price += obj.product.get_discount_price()
            obj.save() # CartProduct.save()
            self.save() # Cart.save()
        else:
            self.total_price -= obj.product.get_discount_price()
            self.total_quantity -= 1
            obj.quantity -= 1
            obj.price -= obj.product.get_discount_price()
            obj.save() # CartProduct.save()
            self.save() # Cart.save()