from django.urls import path
from  . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/', views.payment, name='payment'),
]

