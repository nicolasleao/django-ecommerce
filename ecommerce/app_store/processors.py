from .models import Store, Category
from .selectors import get_user_cart


# Context processors
def shopping_cart_processor(request):
    store_name = request.resolver_match.kwargs['store_name']
    # Try to get the 'cart' instance associated with the current user from the database
    try:
        cart = get_user_cart(request, store_name)
    except:
        # If no cart instance was found in request.COOKIES, return empty cart
        cart = None

    return {'cart': cart}


def categories_processor(request):
    store_name = request.resolver_match.kwargs['store_name']
    store = Store.objects.get(name=store_name)
    # Make queries
    categories_on_navbar = 3
    # Get the first n categories on database, n = categories_on_navbar
    categories = Category.objects.filter(store=store)[:categories_on_navbar]
    # Get the last n categories on database
    categories_more = Category.objects.all()[categories_on_navbar:]
    return {'categories': categories, 'categories_more': categories_more}


def update_context(request, context):
    context.update(shopping_cart_processor(request))
    context.update(categories_processor(request))
    return context
