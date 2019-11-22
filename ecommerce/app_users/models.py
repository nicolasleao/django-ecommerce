from django.contrib.auth.models import AbstractUser
from django.db import models
from .utils import user_avatar_path


# Create your models here.
class CustomUser(AbstractUser):
	avatar = models.ImageField(blank=True, upload_to=user_avatar_path)
