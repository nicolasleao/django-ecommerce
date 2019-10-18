from django.db import models
from store.models import Store, Product
from users.models import CustomUser


# Create your models here.
class Plan(models.Model):
	def __str__(self):
		return self.name
	name = models.CharField(max_length=60, default='')
	price = models.FloatField()
	duration_days = models.PositiveIntegerField()
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)


class Subscription(models.Model):
	def __str__(self):
		return 'SUBSCRIPTION-'+self.store.name+'-'+self.plan.name
	store = models.ForeignKey(Store, on_delete=models.CASCADE)
	plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)


class Invoice(models.Model):
	def __str__(self):
		return 'INVOICE-'+self.subscription.store.name+'-'+self.subscription.plan.name+'-'+str(self.emission_date)
	subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
	price = models.FloatField()
	emission_date = models.DateTimeField(auto_now_add=True)
	expiration_date = models.DateTimeField()


class Payment(models.Model):
	def __str__(self):
		return 'PAYMENT-'+self.invoice.subscription.store.name+'-'+self.invoice.subscription.plan.name+'-'+str(self.date_created)
	invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
	price = models.FloatField()
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

class Purchase(models.Model):
	def __str__(self):
		return 'PURCHASE-'+self.user.username+'-'+self.store.name
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	store = models.ForeignKey(Store, on_delete=models.CASCADE)
	total_price = models.FloatField()
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

class Item(models.Model):
	def __str__(self):
		return 'ITEM-'+self.purchase.store.name+'-'+self.product.name
	purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)