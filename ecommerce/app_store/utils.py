# Media upload path factory methods
def product_thumbnail_path(instance, filename):
    return '{}/products/images/{}'.format(instance.category.store.name, filename)
