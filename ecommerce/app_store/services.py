from .models import Product, Discount
from .selectors import get_user_cart


def add_item(request, store_name, product_id):
    # Make queries
    cart = get_user_cart(request, store_name)
    product = Product.objects.get(pk=product_id)

    for item in cart['items']:
        if str(item[0]) == str(product_id):
            item[2] += 1
            request.session[store_name] = cart
            request.session.modified = True

            return cart['total_items']

    new_product = (product.id, product.slug, 1)

    # Update session to contain the new items in cart
    cart['items'].append(new_product)
    cart['total_items'] += 1
    request.session[store_name] = cart
    request.session.modified = True

    return cart['total_items']


def remove_item(request, store_name, product_id):
    cart = get_user_cart(request, store_name)

    for item in cart['items']:
        if str(item[0]) == str(product_id):
            cart['items'].remove(item)
            cart['total_items'] -= 1
            request.session[store_name] = cart
            request.session.modified = True
            # Return True on successful deletion
            return True
    # Return False on failure
    return False


def update_item_quantity(request, store_name, product_id, quantity):
    cart = get_user_cart(request, store_name)

    for item in cart['items']:
        if str(item[0]) == str(product_id):
            item[2] = int(quantity)
            request.session[store_name] = cart
            request.session.modified = True
            # Return True on successful update
            return True
    # Return False on failure
    return False


def calculate_discount(coupon, total):
    try:
        instance = Discount.objects.get(code=coupon)
        discounted_value = total * (instance.percentage/100)
        return total - discounted_value, discounted_value
    except Discount.DoesNotExist:
        return total, 0


def calculate_cart_total(request, store_name):
    """Returns the total price in the shopping cart"""
    cart = get_user_cart(request, store_name)
    total = 0.00
    # Go through each item inside the user's cart and add it's quantity * price to the cart total
    for item in cart['items']:
        instance = Product.objects.get(pk=item[0])
        total += instance.price_new * item[2]
    return total
