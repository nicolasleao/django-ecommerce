from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from django.views.generic.base import View
from django.views.generic.list import ListView
from .models import Product, Cart

# TODO: update cart views to use ajax (django-ajax package)

@login_required
def get_user_cart(request):
    try:
        # Try to get existing cart instance assigned to current user
        cart = Cart.objects.get(user=request.user)
        return cart
    except Cart.DoesNotExist:
        # If user has no Cart instance, create a new one and associate to request.user
        cart = Cart.objects.create(user=request.user)
        return cart

def get_cart_text(items):
    # Generate cart items text by appending 'item' or 'items' to the value
    if (items == 1):
        cart_items_text = str(items) + " item"
    else:
        cart_items_text = str(items) + " itens"
    return cart_items_text

class AddToCart(View):
    def get(self, request, product_id):
        # Get or create a cart assigned to the current user
        cart = get_user_cart(request)
        # Use the Cart model's add_item() method to update cart in database
        cart.add_item(product_id)
        # Use the Cart model's total_items() method to get the new ammount of items
        total_cart_items = cart.get_total_items()
        # Generate a new cart text to update the html page
        cart_text = get_cart_text(total_cart_items)

        return JsonResponse({'cart_text': cart_text})


class RemoveFromCart(View):
    def get(self, request, item_id):
        # Remove product from cart
        cart = get_user_cart(request)
        item = cart.remove_item(item_id)
        # Redirect to shopping cart
        return redirect('shopping-cart')


# Index page for regular users and guests
class StoreHome(View):
    def get(self, request, *args, **kwargs):
        # Get top sellers
        top_sellers = Product.objects.all().order_by('total_sales')[:4]
        context = {
            'top_sellers': top_sellers,
            'test': '<p>estou testando</p>'
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

class CRUDView(View):
    # Define all allowed HTTP methods to allow CRUD operations while blocking suspicious requests
    http_method_names = ['get', 'post', 'put', 'delete']
    read_template = 'app_store/default_read_template.html'
    create_template = 'app_store/default_create_template.html'
    update_template = 'app_store/default_update_template.html'
    delete_template = 'app_store/default_delete_template.html'

    def http_method_not_allowed(self, request, *args, **kwargs):
        raise PermissionDenied

    def get(self, request):
        return HttpResponse("read")

    def post(self, request):
        return HttpResponse("create")

    def put(self, request):
        return HttpResponse("update")

    def delete(self, request):
        return HttpResponse("delete")