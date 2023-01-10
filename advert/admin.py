from django.contrib import admin
from advert.models import Advert, AdvertImage


class AdvertImageInLine(admin.TabularInline):
    model = AdvertImage
    extra = 3


class AdvertAdmin(admin.ModelAdmin):
    inlines = [AdvertImageInLine, ]


admin.site.register(Advert, AdvertAdmin)
