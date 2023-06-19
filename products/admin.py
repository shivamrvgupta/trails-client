from django.contrib import admin
from .models import Product, Cart, Order, Coupon
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'dicount', 'is_on_sale', 'price', 'sale_price')
    list_display_links = ('id', 'title',)
    list_editable = ('is_published', 'is_on_sale')
    search_fields = ('title', 'description', 'price')
    list_per_page = 25


admin.site.register(Product, ProductAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity','price','total_amt')
    list_display_links = ('id', 'product')
    list_per_page = 25

admin.site.register(Cart, CartAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product')
    list_display_links = ('id', 'product')
    list_per_page = 25


admin.site.register(Order, OrderAdmin)


class CouponAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'coupon_price', 'is_valid')
    list_display_links = ('id', 'title')
    list_per_page = 25


admin.site.register(Coupon, CouponAdmin)
