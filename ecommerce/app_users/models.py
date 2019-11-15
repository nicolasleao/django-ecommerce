import hashlib
from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
	# User token for authentication, a new one should be generated using the generate_token() method whenever it is used
	token = models.CharField(max_length=64, default="")

	def __str__(self):
		return self.email

	def email_domain(self):
		return self.email.split('@')[1]

	def generate_token(self):
		base_string = self.email + datetime.now().strftime()
		new_token = hashlib.sha256(base_string).hexdigest()
		self.token = new_token
		self.save()

	def get_token(self):
		token = self.token
		self.generate_token()
		return token
