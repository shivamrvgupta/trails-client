from django.urls import path
from  . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('listings/', views.listings, name='listings'),
    path('delete/<int:id>/', views.delete_data, name='delete_data'),
]

