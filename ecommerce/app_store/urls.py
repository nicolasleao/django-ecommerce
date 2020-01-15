from django.urls import path

from . import views

urlpatterns = [
    # Store routes
    path('<str:store_name>/', views.StoreHome.as_view(), name='store-home'),
    path('<str:store_name>/cart/', views.ShoppingCart.as_view(), name='shopping-cart'),
    path('<str:store_name>/search/', views.ProductSearchView.as_view(), name='product-list'),
    path('<str:store_name>/<str:category_name>/search/', views.ProductSearchView.as_view(), name='product-list'),

    # Checkout routes
    path('<str:store_name>/checkout/', views.Checkout, name='checkout'),

    # AJAX views
    path('<str:store_name>/add-to-cart/<str:product_id>/', views.AddToCart.as_view(), name='add-to-cart'),
    path('<str:store_name>/remove-from-cart/<str:product_id>/', views.RemoveFromCart.as_view(),
         name='remove-from-cart'),
    path('<str:store_name>/update-item-quantity/<str:product_id>/<int:quantity>/', views.UpdateItemQuantity.as_view(),
         name='update-item-quantity'),

]
