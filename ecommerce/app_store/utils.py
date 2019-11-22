# Media upload path factory methods
def product_thumbnail_path(instance):
    return '{}/products/images/{}'.format(instance.category.store.name, instance.image.filename)