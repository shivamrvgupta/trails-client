from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.



class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    dicount = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/products/%Y/%m/%d/')
    small_photo = models.ImageField(upload_to='photos/carts/%Y/%m/%d/')
    is_on_sale = models.BooleanField(default=True)
    is_published = models.BooleanField(default=True)
    is_out_of_stock = models.BooleanField(default=False)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    modified_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def get_amount_after_discount(self):
        sale_price = self.price - (self.price * self.dicount / 100)
        print('price after sale -- {}'.format(sale_price))
        return int(sale_price)
    sale_price = property(get_amount_after_discount)


class Cart(models.Model):
    small_photo = models.ImageField(upload_to='photos/carts/%Y/%m/%d/', blank=True)
    user = models.CharField(max_length=200,default=None)
    product = models.CharField(max_length=200,default=None)
    quantity = models.IntegerField(blank=True)
    price = models.IntegerField(default=0)
    modified_date = models.DateTimeField(default=datetime.now, blank=True)


    def get_amount_after_quantity(self):
        total_amt = self.quantity * self.price
        return round(total_amt) 
    total_amt = property(get_amount_after_quantity)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    ordered_date = models.DateTimeField(default=datetime.now, blank=True)
    
class Coupon(models.Model):
    title = models.CharField(max_length=200)
    coupon_price = models.IntegerField()
    is_valid = models.BooleanField(default=True)
    discounted_price = models.IntegerField()

class Customs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    desc = models.TextField(max_length=1000)
    refimg = models.ImageField(blank=True)
