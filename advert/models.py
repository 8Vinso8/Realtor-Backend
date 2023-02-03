from django.db import models
from django.conf import settings
from django.utils import timezone


class Advert(models.Model):
    class AdvertType(models.TextChoices):
        APARTMENT = 'Квартира'
        HOUSE = 'Дом'
        Land = 'Земельный участок'

    advert_type = models.CharField(
        max_length=20, choices=AdvertType.choices, default=AdvertType.Land)

    city = models.TextField(max_length=200, blank=True)
    street = models.TextField(max_length=200, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    address = models.TextField(max_length=200, blank=True)
    floor = models.IntegerField(null=True, blank=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, related_name='adverts')

    title = models.TextField(blank=False)
    description = models.TextField(blank=True)
    sold = models.BooleanField(default=False)

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
