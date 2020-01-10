from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic.base import View
from django.views.generic.list import ListView

from ..models import Product
from ..selectors import find_products, get_top_sellers, get_store_id, get_user_cart
from ..services import calculate_discount


# TODO: update cart views to use cookies


class StoreHome(View):
    """Displays customized homepage matching the current Store model settings"""

    def get(self, request, *args, **kwargs):
        for product in Product.objects.all():
            product.save()
        # Make necessary queries
        store_id = get_store_id(request)
        top_sellers = get_top_sellers(store_id, 4)

        # Render template
        context = {
            'top_sellers': top_sellers,
        }
        return render(request, 'app_store/store_home.html', context)


class ProductSearchView(ListView):
    """Displays results for user search query 'q' """
    paginate_by = 30

    def get_queryset(self):
        query = self.request.GET.get('q')
        store_id = get_store_id(self.request)
        # Make the necessary query and use it as queryset for this ListView instance
        return find_products(store_id, query)

    def get_context_data(self, **kwargs):
        # Get search query and category
        query = self.request.GET.get('q')
        if 'category_name' in self.kwargs:
            category = self.kwargs['category_name']
        else:
            category = None

        context = super().get_context_data(**kwargs)
        # Append additional items to the context of the parent class
        context['now'] = timezone.now()
        context['query'] = query
        context['category'] = category
        return context


class ShoppingCart(View):
    """Displays the user's shopping cart and order summary for the current store"""
    def get(self, request):
        # Make necessary queries, populate cart with product instances and calculate total
        cart = get_user_cart(request)
        items = []
        total = 0
        for item in cart['items']:
            instance = get_object_or_404(Product, pk=str(item[0]))
            total += instance.price_new
            # Each item is stored in a list, with the information stored in the following order
            # [product_instance, product_quantity, product_total]
            items.append([instance, item[2], item[2] * instance.price_new])

        coupon = request.GET.get('coupon')
        total, discount = calculate_discount(coupon, total)
        context = {
            'items': items,
            'total': total,
            'discount': discount,
        }
        return render(request, 'app_store/shopping_cart.html', context)


class Checkout(View):
    def get(self, request):
        return HttpResponse('Checkout view goes here')
