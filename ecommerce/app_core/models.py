from django.contrib.auth.models import AbstractUser
from django.db import models

from .utils import user_avatar_path


class CustomUser(AbstractUser):
    avatar = models.ImageField(blank=True, upload_to=user_avatar_path)


class Postable(models.Model):
    name = models.CharField(max_length=150, default='')
    visible = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

