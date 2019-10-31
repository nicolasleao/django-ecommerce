from django.db import models
from django.utils import timezone
from users.models import CustomUser

# TODO:
# Allow users to save carts
# Add configuration fields to STORE

def ProductThumbnailPath(instance):
	return '{}/products/images/{}'.format(instance.category.store.name, instance.image.filename)


class Store(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	name = models.CharField(max_length=60, unique=True, default='')
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Category(models.Model):
	store = models.ForeignKey(Store, on_delete=models.CASCADE)
	name = models.CharField(max_length=60, default='')
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Collection(models.Model):
	store = models.ForeignKey(Store, on_delete=models.CASCADE)
	name = models.CharField(max_length=60, default='')
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Product(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
	collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
	name = models.CharField(max_length=60, default='')
	description = models.TextField(max_length=1200, default='')
	model = models.CharField(max_length=100, default='')
	price_new = models.FloatField(default=0)
	price_old = models.FloatField(default=0)
	image = models.ImageField()
	total_sales = models.PositiveIntegerField(default=0, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	# TODO: Add colors and sizes manytomany

	def __str__(self):
		return self.name


class Discount(models.Model):
	products = models.ManyToManyField(Product)
	code = models.CharField(max_length=60, default='')
	percentage = models.FloatField(default=0)
	expiration_date = models.DateTimeField(default=timezone.now)
	products = models.ManyToManyField(Product)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.code


class Cart(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return 'CART-'+self.user.username+'-'+str(self.date_created)

	def get_total_items(self):
		print("ora")
		print(self.item_set.count())
		return self.item_set.count()

	def get_total(self):
		total = 0
		# Iterate through all items that have this cart referenced as foreign key
		for item in self.cartitem__set.all():
			# Add current item's total price to the 'total' variable
			total += item.get_total()

		return total

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
		except:
			return None

		# Return the new Item instance if it was successfully created
		return new_item

	def remove_item(self, item_id):
		# Try to get and delete item instance
		try:
			deleted_item = Item.objects.get(pk=item_id)
			deleted_item.delete()
		# Return false on failure
		except:
			return None

		# Return True on success
		return deleted_item

class Item(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='item_product')
	quantity = models.PositiveIntegerField(default=1)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return 'CART_PRODUCT-'+self.cart.user.username+'-'+self.product.name

	def get_total(self):
		return self.quantity * self.product.price_new