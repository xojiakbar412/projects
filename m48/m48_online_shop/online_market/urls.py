
from django.contrib import admin
from django.urls import path
from online_market import views

urlpatterns = [
    path('online_market/', views.product_list, name='product_list'),
    path('categories/', views.categories, name='categories'),
    path('product-detail//<int:product_id>/', views.product_detail, name='product_detail'),
]
