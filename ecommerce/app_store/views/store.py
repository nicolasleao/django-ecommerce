from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.generic.base import View
from django.views.generic.list import ListView
from ..selectors import find_products, get_top_sellers, get_store_id

# TODO: update cart views to use ajax (django-ajax package)


# Index page for regular users and guests
class StoreHome(View):
    """Displays customized homepage matching the current Store model settings"""
    def get(self, request, *args, **kwargs):
        # Make necessary queries
        store_id = get_store_id(request)
        top_sellers = get_top_sellers(store_id, 4)

        # Render template
        context = {
            'top_sellers': top_sellers,
        }
        return render(request, 'app_store/store_home.html', context)


# Query products with a querystring 'q'
class ProductSearchView(ListView):
    """Displays results for user search query"""
    paginate_by = 30

    def get_queryset(self):
        query = self.request.GET.get('q')
        # Make the necessary query and use it as queryset for this ListView instance
        return find_products(query)

    def get_context_data(self, **kwargs):
        # Get search query and category
        query = self.request.GET.get('q')
        if 'category_name' in self.kwargs:
            category = self.kwargs['category_name']

        context = super().get_context_data(**kwargs)
        # Append additional items to the context of the parent class
        context['now'] = timezone.now()
        context['query'] = query
        context['category'] = category
        return context


class ShoppingCart(View):
    """Displays the user's shopping cart and order summary for the current store"""
    def get(self, request):
        context = {}
        return render(request, 'app_store/shopping_cart.html', context)


class Checkout(View):
    def get(self, request):
        return HttpResponse('Checkout view goes here')
