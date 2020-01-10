from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic.base import View

from ..selectors import get_user_cart
from ..services import add_item, remove_item


def get_cart_text(items):
    # Generate cart items text by appending 'item' or 'items' to the value
    if (items == 1):
        cart_items_text = str(items) + " item"
    else:
        cart_items_text = str(items) + " itens"
    return cart_items_text


class AddToCart(View):
    """Ajax view that adds item to user's cart and returns json response with cart quantity"""
    def get(self, request, product_id):
        # Get or create a cart assigned to the current user
        cart = get_user_cart(request)
        # Use services.add_item() method to update cart in user session
        add_item(request, product_id)
        # Use the Cart model's total_items() method to get the new ammount of items
        total_cart_items = 1
        # Generate a new cart text to update the html page
        cart_text = get_cart_text(total_cart_items)

        return JsonResponse({'cart_text': cart_text})


class RemoveFromCart(View):
    def get(self, request, item_id):
        # Remove product from cart
        cart = get_user_cart(request)
        remove_item(request, item_id)
        # Redirect to shopping cart
        return redirect('shopping-cart')