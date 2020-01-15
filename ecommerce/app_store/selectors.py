from django.http import Http404

from .models import Store, Product


def get_store(store_name):
    """Returns the Store instance matching the current store_name"""
    try:
        store = Store.objects.get(name=store_name)
        return store
    except Store.DoesNotExist:
        raise Http404


def get_user_cart(request, store_name):
    """Retrieves cart in the present session, or creates an empty cart object"""
    if store_name in request.session:
        cart = request.session[store_name]
        return cart
    else:
        cart = {
            'total_items': 0,
            'items': [],
        }
        request.session[store_name] = cart
        # Tell django to save changes to the database
        request.session.modified = True
        return cart


def find_products(store_id, category, query):
    if query is None:
        if category is None:
            return Product.objects.filter(store__id=store_id)
        else:
            return Product.objects.filter(store__id=store_id, category=category)
    else:
        if category is None:
            return Product.objects.filter(store__id=store_id, name__icontains=query)
        else:
            return Product.objects.filter(store__id=store_id, category=category, name__icontains=query)


def get_top_sellers(store_id, limit):
    return Product.objects.filter(store__id=store_id).order_by('total_sales')[:limit]