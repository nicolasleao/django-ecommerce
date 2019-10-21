from django.template import RequestContext, Template
from store.models import Cart


def shopping_cart_processor(request):
	# Try to get the 'cart' instance associated with the current user from the database
	try:
		cart = Cart.objects.get(user=request.user)
	except:
		# If no cart instance was found in request.COOKIES, return empty cart
		cart = {
			'user': '',
			'products': [],
		}

    return {'cart': cart}