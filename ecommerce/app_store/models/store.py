from django.db import models
from django.conf import settings
from django.utils import timezone
from app_core.models import Postable
from ..utils import product_thumbnail_path


class Store(Postable):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, unique=True, default='')
    domain = models.CharField(max_length=150, unique=True, default='')


class StoreContent(Postable):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)


class Category(StoreContent):
    pass


class Product(StoreContent):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    description = models.TextField(max_length=1200, default='')
    model = models.CharField(max_length=100, default='')
    price_new = models.FloatField(default=0)
    price_old = models.FloatField(default=0)
    image = models.ImageField(upload_to=product_thumbnail_path)
    total_sales = models.PositiveIntegerField(default=0, blank=True)

    # TODO: Create product types


class Collection(StoreContent):
    products = models.ManyToManyField(Product)


class Discount(StoreContent):
    code = models.CharField(max_length=60, default='')
    percentage = models.FloatField(default=0)
    expiration_date = models.DateTimeField(default=timezone.now)
    products = models.ManyToManyField(Product)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.code
