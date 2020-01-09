import json

from django.forms.models import model_to_dict
from django.shortcuts import redirect

from .models import Product
from .selectors import get_store_name


def get_user_cart(request):
    """Retrieves cart in the present session, or creates an empty cart object"""
    store_name = get_store_name(request)
    print("STORENAME" + store_name)
    if store_name in request.session:
        cart = request.session[store_name]
        print("Cart")
        print(cart)
        return cart
    else:
        cart = {
            'total_items': 0,
            'items': [],
        }
        request.session[store_name] = cart
        # Tell django to save changes to the database
        request.session.modified = True
        print("Cart")
        print(cart)
        return cart


def add_item(request, product_id):
    # Make queries
    cart = get_user_cart(request)
    store_name = get_store_name(request)
    product = Product.objects.get(pk=product_id)

    session_product = (product.id, product.slug, 1)

    # Update session to contain the new items in cart
    cart['items'].append(session_product)
    request.session[store_name] = cart
    request.session.modified = True

    return {'quantity': 1}


def remove_item(self, item_id):
    # Try to get and delete item instance
    try:
        pass
        # deleted_item = Item.objects.get(pk=item_id)
        # deleted_item.delete()
    # Return false on failure
    except AssertionError:  # Item.DoesNotExist:
        return None

    # Return True on success
    # return deleted_item
