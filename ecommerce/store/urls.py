from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('store/', views.StoreLanding.as_view(), name='store-landing'),
    path('store/search', views.ProductSearchView.as_view(), name='product-list'),
]
