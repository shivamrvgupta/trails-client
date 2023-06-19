from django.urls import path
from . import views

urlpatterns = [
    path('trying/', views.trying, name="trying"),
]