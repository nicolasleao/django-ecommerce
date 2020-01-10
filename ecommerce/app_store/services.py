from .models import Product, Discount
from .selectors import get_store_name, get_user_cart


def add_item(request, product_id):
    # Make queries
    cart = get_user_cart(request)
    store_name = get_store_name(request)
    product = Product.objects.get(pk=product_id)

    for item in cart['items']:
        if str(item[0]) == str(product_id):
            item[2] += 1
            request.session[store_name] = cart
            request.session.modified = True

            return {'quantity': item[2]}

    new_product = (product.id, product.slug, 1)

    # Update session to contain the new items in cart
    cart['items'].append(new_product)
    cart['total_items'] += 1
    request.session[store_name] = cart
    request.session.modified = True

    return {'quantity': 1}


def remove_item(request, product_id):
    # Make queries
    cart = get_user_cart(request)
    store_name = get_store_name(request)

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


def calculate_discount(coupon, total):
    try:
        instance = Discount.objects.get(code=coupon)
        discounted_value = total * (instance.percentage/100)
        return total - discounted_value, discounted_value
    except Discount.DoesNotExist:
        return total, 0
