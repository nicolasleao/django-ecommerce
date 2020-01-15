from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic.base import View
from django.views.generic.list import ListView

from ..models import Product
from ..processors import update_context
from ..selectors import find_products, get_top_sellers, get_store, get_user_cart
from ..services import calculate_discount


# TODO: update cart views to use cookies


class StoreHome(View):
    """Displays customized homepage matching the current Store model settings"""

    def get(self, request, *args, **kwargs):
        for product in Product.objects.all():
            product.save()
        # Make necessary queries
        store_name = kwargs['store_name']
        store = get_store(store_name)
        top_sellers = get_top_sellers(store.id, 4)

        # Render template
        context = {
            'store_name': store_name,
            'top_sellers': top_sellers,
        }
        context = update_context(request, context)
        return render(request, 'app_store/store_home.html', context)


class ProductSearchView(ListView):
    """Displays results for user search query 'q' """
    paginate_by = 30

    def get_queryset(self):
        store_name = self.kwargs['store_name']
        query = self.request.GET.get('q')
        store = get_store(store_name)
        if 'category_name' in self.kwargs:
            category = self.kwargs['category_name']
        else:
            category = None
        # Make the necessary query and use it as queryset for this ListView instance
        return find_products(store.id, category, query)

    def get_context_data(self, **kwargs):
        # Get search store_name, query, and category
        store_name = self.kwargs['store_name']
        query = self.request.GET.get('q')
        if 'category_name' in self.kwargs:
            category = self.kwargs['category_name']
        else:
            category = None

        context = super().get_context_data(**kwargs)
        # Append additional items to the context of the parent class
        context['store_name'] = store_name
        context['now'] = timezone.now()
        context['query'] = query
        context['category'] = category
        context = update_context(self.request, context)
        return context


class ShoppingCart(View):
    """Displays the user's shopping cart and order summary for the current store"""

    def get(self, request, *args, **kwargs):
        # Make necessary queries, populate cart with product instances and calculate total
        store_name = kwargs['store_name']
        cart = get_user_cart(request, store_name)
        items = []
        total = 0
        for item in cart['items']:
            instance = get_object_or_404(Product, pk=str(item[0]))
            total += instance.price_new * item[2]
            # Each item is stored in a list, with the information stored in the following order
            # [product_instance, product_quantity, product_total]
            items.append([instance, item[2], item[2] * instance.price_new])

        coupon = request.GET.get('coupon')
        total, discount = calculate_discount(coupon, total)
        context = {
            'store_name': store_name,
            'items': items,
            'total': total,
            'discount': discount,
        }
        context = update_context(request, context)
        return render(request, 'app_store/shopping_cart.html', context)


class Checkout(View):
    def get(self, request):
        return HttpResponse('Checkout view goes here')
