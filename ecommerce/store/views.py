from django.shortcuts import render
from allauth.account.forms import LoginForm
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.base import View
from .models import Product, Category, Cart


	# TODO: Allow users to save multiple carts


# Index page for regular users and guests
class StoreLanding(View):

    def get(self, request, *args, **kwargs):
        # Make queries
        categories = Category.objects.all()[:3]
        categories_more = Category.objects.all()[3:]
        top_sellers = [{'name': 'Camiseta branca', 'price': 45.0},
                       {'name': 'Camiseta preta', 'price': 50.0},
                       {'name': 'Camiseta azul', 'price': 45.0},
                       {'name': 'Jeans desbotada', 'price': 70.0}]

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
        return render(request, 'store/store.html', context)


# A Django ListView that queries products by a querystring 'q'
class ProductSearchView(ListView):

    paginate_by = 30

    # Fetch query string from request.GET
    def get_queryset(self):
        return Product.objects.filter(name__icontains=self.request.GET.get('q'))

    # Define context for the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['query'] = self.request.GET.get('q')
        context['categories'] = Category.objects.all()
        return context