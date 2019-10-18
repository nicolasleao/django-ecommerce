from django.db import models
from django.utils import timezone
from users.models import CustomUser

def ProductThumbnailPath(instance):
	return '{}/products/images/{}'.format(instance.category.store.name, instance.image.filename)

# Create your models here.
class Store(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	name = models.CharField(max_length=60, unique=True, default='')
	# TODO: add configuration fields
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)


class Category(models.Model):
	store = models.ForeignKey(Store, on_delete=models.CASCADE)
	name = models.CharField(max_length=60, default='')
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)


class Collection(models.Model):
	store = models.ForeignKey(Store, on_delete=models.CASCADE)
	name = models.CharField(max_length=60, default='')
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)


class Product(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
	collection = models.ForeignKey(Category, on_delete=models.CASCADE)
	name = models.CharField(max_length=60, default='')
	description = models.TextField(max_length=1200, default='')
	model = models.CharField(max_length=100, default='')
	color = models.CharField(max_length=20, default='')
	size = models.CharField(max_length=20, default='')
	price_new = models.FloatField(default=0)
	price_old = models.FloatField(default=0)
	image = models.ImageField()
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)


class Discount(models.Model):
	products = models.ManyToManyField(Product)
	code = models.CharField(max_length=60, default='')
	percentage = models.FloatField(default=0)
	expiration_date = models.DateTimeField(default=timezone.now)
	products = models.ManyToManyField(Product)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)