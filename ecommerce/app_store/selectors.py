from .models import Store, Product


def get_store(request):
    """Returns the Store instance matching the current domain"""

    # TODO: remove [:-5] suffix in production

    current_domain = request.META['HTTP_HOST'][:-5]
    # .only(<column>) ensures that the ORM selects only the desired column, simplifying the query
    store = Store.objects.get(domain=current_domain)
    return store


def get_store_name(request):
    """Returns name of the Store instance matching the current domain"""
    current_domain = request.META['HTTP_HOST'][:-5]
    # .only(<column>) ensures that the ORM selects only the desired column, simplifying the query
    store = Store.objects.get(domain=current_domain).name
    return store


def get_store_id(request):
    """Returns id of the Store instance matching the current domain"""
    current_domain = request.META['HTTP_HOST'][:-5]
    # .only(<column>) ensures that the ORM selects only the desired column, simplifying the query
    store = Store.objects.get(domain=current_domain).id
    return store


def get_user_cart(request):
    """Returns a python dictionary that represents the user's cart for the current store"""

    # TODO: Recreate this function to use cookies

    store = get_store(request)
    print(store)
    print(store.name)
    print(request.COOKIES.get(store.name))


def find_products(store_id, query):
    return Product.objects.filter(store__id=store_id, name__icontains=query)


def get_top_sellers(store_id, limit):
    return Product.objects.filter(store__id=store_id).order_by('total_sales')[:limit]