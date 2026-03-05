from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('branches/', views.branches, name='branches'),
    path('branches/<int:id>/', views.branch_detail, name='branch_detail'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
]