from django.db import models
from django.conf import settings
from django.utils import timezone


class Advert(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, related_name='adverts')

    title = models.TextField(blank=False)
    address = models.TextField(max_length=200, blank=False)
    description = models.TextField(blank=True)
    
    date = models.DateField(default=timezone.now)
    price = models.IntegerField(blank=False)
    preview = models.ImageField()
    
    class Meta:
        ordering = ['date']

    def __str__(self) -> str:

       return self.title


class AdvertImage(models.Model):
    advert = models.ForeignKey(Advert, related_name='images',
                               on_delete=models.CASCADE)
    image = models.ImageField()
