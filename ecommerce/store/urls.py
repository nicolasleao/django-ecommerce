from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
	# Store routes
    path('store/', views.StoreLanding.as_view(), name='store-landing'),
    path('store/search/<str:category_id>/', views.ProductSearchView.as_view(), name='product-list'),

    # Checkout routes
    path('checkout/', views.Checkout, name='checkout'),

    # AJAX views
    path('add-to-cart/', views.AddToCart.as_view(), name='add-to-cart'),
    path('remove-from-cart/', views.RemoveFromCart.as_view(), name='remove-from-cart'),

]
