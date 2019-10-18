from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.StoreLanding, name='StoreLanding'),
    path('search/<str:category_id>', views.StoreSearch, name='StoreSearch'),
]
