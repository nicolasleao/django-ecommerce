from app_store.models import Category
from app_store.services import get_user_cart

# TODO:
# Working category_name_processor


def shopping_cart_processor(request):
    # Try to get the 'cart' instance associated with the current user from the database
    try:
        cart = get_user_cart(request)
    except:
        # If no cart instance was found in request.COOKIES, return empty cart
        cart = None

    return {'cart': cart}


def categories_processor(request):
    # Make queries
    categories_on_navbar = 3
    # Get the first n categories on database, n = categories_on_navbar
    categories = Category.objects.all()[:categories_on_navbar]
    # Get the last n categories on database
    categories_more = Category.objects.all()[categories_on_navbar:]
    return {'categories': categories, 'categories_more': categories_more}
