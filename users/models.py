from django.contrib.auth.models import AbstractUser
from django.db import models

from advert.models import Advert


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=30, verbose_name="Телефон", blank=True)
    favorite_adverts = models.ManyToManyField(to=Advert, blank=True, related_name="favorite_adverts", verbose_name="Избранные объявления")
    is_realtor = models.BooleanField(default=False)
    clients = models.ManyToManyField("self", blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    def __str__(self):
        return self.username

    REQUIRED_FIELDS = ['phone']
