from django.shortcuts import redirect
from .models import Product
from .selectors import get_store_name
import json


def get_user_cart(request):
    """Retrieves cart in the present session, or creates an empty cart object"""
    store_name = get_store_name(request)
    if store_name in request.session:
        cart = request.session[store_name]
        return cart
    else:
        cart = {
            'total_items': 0,
            'items': {},
        }
        request.session[store_name] = cart
        # Tell django to save changes to the database
        request.session.modified = True
        return cart


def add_item(self, product_id):
    # Try to get the product
    try:
        product = Product.objects.get(pk=product_id)
        # Check if product is already on cart, if so increment item.quantity
        try:
            pass
            # item = Item.objects.get(cart=self, product=product)
            # item.quantity += 1
            # item.save()
            # return item
        # If product is not already in cart create a new Item instance
        except AssertionError:  # Item.DoesNotExist:
            pass
            # new_item = Item.objects.create(cart=self, product=product, quantity=1)
    # Return None on failure
    except Product.DoesNotExist:
        return None

    # Return the new Item instance if it was successfully created
    # return new_item


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
