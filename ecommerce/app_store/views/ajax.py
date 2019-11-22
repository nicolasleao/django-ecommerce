from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic.base import View
from ..selectors import get_user_cart


def get_cart_text(items):
    # Generate cart items text by appending 'item' or 'items' to the value
    if (items == 1):
        cart_items_text = str(items) + " item"
    else:
        cart_items_text = str(items) + " itens"
    return cart_items_text


class AddToCart(View):
    def get(self, request, product_id):
        # Get or create a cart assigned to the current user
        cart = get_user_cart(request)
        # Use the Cart model's add_item() method to update cart in database
        cart.add_item(product_id)
        # Use the Cart model's total_items() method to get the new ammount of items
        total_cart_items = cart.total_items
        # Generate a new cart text to update the html page
        cart_text = get_cart_text(total_cart_items)

        return JsonResponse({'cart_text': cart_text})


class RemoveFromCart(View):
    def get(self, request, item_id):
        # Remove product from cart
        cart = get_user_cart(request)
        item = cart.remove_item(item_id)
        # Redirect to shopping cart
        return redirect('shopping-cart')