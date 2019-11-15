from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic.base import View
from django.views.generic.list import ListView

from .models import Product, Cart


# TODO: update cart views to use ajax (django-ajax package)

@login_required
def get_user_cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
        return cart
    except Cart.DoesNotExist:
        # If user has no Cart instance, create a new one and associate to request.user
        cart = Cart.objects.create(user=request.user)
        return cart

class AddToCart(View):
    def post(self, request):
        # Add product to cart
        cart = get_user_cart(request)
        product_id = request.POST.get('product_id')
        item = cart.add_item(product_id)
        print("added item "+item.product.name)
        # Redirect to store homepage
        return redirect('store-home')


class RemoveFromCart(View):
    def post(self, request):
        # Remove product from cart
        cart = get_user_cart(request)
        item_id = request.POST.get('item_id')
        item = cart.remove_item(item_id)
        print("removed item "+item.product.name)
        # Redirect to store homepage
        return redirect('store-home')


# Index page for regular users and guests
class StoreHome(View):
    def get(self, request, *args, **kwargs):
        # Get top sellers
        top_sellers = Product.objects.all().order_by('total_sales')[:4]
        context = {
            'top_sellers': top_sellers,
        }
        return render(request, 'app_store/store_home.html', context)


# Query products with a querystring 'q'
class ProductSearchView(ListView):
    paginate_by = 30

    # Fetch query string from request.GET
    def get_queryset(self):
        return Product.objects.filter(name__icontains=self.request.GET.get('q'))

    # Define context for the template
    def get_context_data(self, **kwargs):
        # Get search query
        query = self.request.GET.get('q')
        # Get current category
        try:
            category = self.kwargs['category_name']
        except:
            category = None

        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['query'] = query
        context['category'] = category
        return context


class ShoppingCart(View):
    def get(self, request):
        context = {}
        return render(request, 'app_store/shopping_cart.html', context)

# Checkout view
def Checkout(request):
    return HttpResponse('Checkout view goes here')