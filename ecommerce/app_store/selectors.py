from .models import Store, Product


def get_store(request):
    """Returns the Store instance matching the current domain"""

    # TODO: remove [:-5] suffix in production

    current_domain = request.META['HTTP_HOST'][:-5]
    store = Store.objects.get(domain=current_domain)
    return store


def get_store_name(request):
    """Returns name of the Store instance matching the current domain"""
    current_domain = request.META['HTTP_HOST'][:-5]
    store_name = Store.objects.get(domain=current_domain).name
    return store_name


def get_store_id(request):
    """Returns id of the Store instance matching the current domain"""
    current_domain = request.META['HTTP_HOST'][:-5]
    store_id = Store.objects.get(domain=current_domain).id
    return store_id


def get_user_cart(request):
    """Retrieves cart in the present session, or creates an empty cart object"""
    store_name = get_store_name(request)
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


def find_products(store_id, query):
    return Product.objects.filter(store__id=store_id, name__icontains=query)


def get_top_sellers(store_id, limit):
    return Product.objects.filter(store__id=store_id).order_by('total_sales')[:limit]