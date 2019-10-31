from django.template import RequestContext, Template
from store.models import Cart

# TODO:
# Working category_name_processor

def shopping_cart_processor(request):
    # Try to get the 'cart' instance associated with the current user from the database
    try:
        cart = Cart.objects.get(user=request.user)
    except:
        # If no cart instance was found in request.COOKIES, return empty cart
        cart = None

    return {'cart': cart}


def category_name_processor(request):
	return None