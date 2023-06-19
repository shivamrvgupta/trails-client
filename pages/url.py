from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('trying', views.trying, name="trying"),
    path('send', views.newsletter, name='newsletter'),
    #path('', views.add_to_cart, name="index"),
]