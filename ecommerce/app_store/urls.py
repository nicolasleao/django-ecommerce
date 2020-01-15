from django.urls import path
from . import views
from django.urls import path

from . import views

urlpatterns = [
	# Store routes
    path('store/', views.StoreHome.as_view(), name='store-home'),
    path('cart/', views.ShoppingCart.as_view(), name='shopping-cart'),
    path('search/<str:category_name>/', views.ProductSearchView.as_view(), name='product-list'),

    # Checkout routes
    path('checkout/', views.Checkout, name='checkout'),

    # AJAX views
    path('add-to-cart/<str:product_id>/', views.AddToCart.as_view(), name='add-to-cart'),
    path('remove-from-cart/<str:product_id>/', views.RemoveFromCart.as_view(), name='remove-from-cart'),
    path('update-item-quantity/<str:product_id>/<str:quantity>/', views.UpdateItemQuantity.as_view(), name='update-item-quantity'),

]
