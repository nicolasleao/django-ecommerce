from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.base import View
from django.forms.models import model_to_dict
from allauth.account.forms import LoginForm
from .models import Product, Category, Cart

# TODO: update cart views to use ajax (django-ajax package)

@login_required
def get_user_cart(request):
    return Cart.objects.get(user=request.user)


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
        # Add product to cart
        cart = get_user_cart(request)
        item_id = request.POST.get('item_id')
        item = cart.remove_item(item_id)
        print("removed item "+item.product.name)
        # Redirect to store homepage
        return redirect('store-home')


# Index page for regular users and guests
class StoreHome(View):

    def get(self, request, *args, **kwargs):
        # Make queries
        categories_on_navbar = 3
        # Get the first n categories on database, n = categories_on_navbar
        categories = Category.objects.all()[:categories_on_navbar]
        # Get the last n categories on database
        categories_more = Category.objects.all()[categories_on_navbar:]

        top_sellers = [{'id': 0, 'name': 'Camiseta preta', 'price': 45.0},
                       {'id': 1, 'name': 'Camiseta branca', 'price': 50.0},
                       {'id': 2, 'name': 'Camiseta azul', 'price': 45.0},
                       {'id': 3, 'name': 'Jeans desbotada', 'price': 70.0}]

        best_reviews = [{'name': 'Camiseta branca', 'price': 45.0},
                        {'name': 'Camiseta preta', 'price': 50.0},
                        {'name': 'Jaqueta preta', 'price': 130.0},
                        {'name': 'Jaqueta azul', 'price': 45.0}]

        context = {
            'categories': categories,
            'categories_more': categories_more,
            'top_sellers': top_sellers,
            'best_reviews': best_reviews,
        }
        return render(request, 'store/store_home.html', context)


# Query products with a querystring 'q'
class ProductSearchView(ListView):

    paginate_by = 30

    # Fetch query string from request.GET
    def get_queryset(self):
        return Product.objects.filter(name__icontains=self.request.GET.get('q'))

    # Define context for the template
    def get_context_data(self, **kwargs):
        # Make queries
        categories_on_navbar = 3
        # Get the first n categories on database, n = categories_on_navbar
        categories = Category.objects.all()[:categories_on_navbar]
        # Get the last n categories on database
        categories_more = Category.objects.all()[categories_on_navbar:]
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
        context['categories'] = categories
        context['categories_more'] = categories_more
        return context

# Checkout view
def Checkout(request):
    return HttpResponse('Checkout view goes here')