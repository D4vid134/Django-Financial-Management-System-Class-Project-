from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name='home'),
    path('stocks/', views.stocks, name='stocks'),
    path('properties/', views.properties, name='properties'),
    path('items/', views.items, name='items'),
    path('buyProperty/<str:pk>/', views.buyProperty, name='buyProperty'),
    path('buyItem/<str:pk>/', views.buyItem, name='buyItem'),
    path('buyStock/<str:pk>/', views.buyStock, name='buyStock'),
    path('assets/', views.assets, name='assets'),
    
]