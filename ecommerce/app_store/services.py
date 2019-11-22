from .models import Product, Item


def add_item(self, product_id):
    # Try to get the product
    try:
        product = Product.objects.get(pk=product_id)
        # Check if product is already on cart, if so increment item.quantity
        try:
            item = Item.objects.get(cart=self, product=product)
            item.quantity += 1
            item.save()
            return item
        # If product is not already in cart create a new Item instance
        except Item.DoesNotExist:
            new_item = Item.objects.create(cart=self, product=product, quantity=1)
    # Return None on failure
    except Product.DoesNotExist:
        return None

    # Return the new Item instance if it was successfully created
    return new_item


def remove_item(self, item_id):
    # Try to get and delete item instance
    try:
        deleted_item = Item.objects.get(pk=item_id)
        deleted_item.delete()
    # Return false on failure
    except Item.DoesNotExist:
        return None

    # Return True on success
    return deleted_item