from django_filters import rest_framework as filters
from advert.models import Advert

class AdvertFilter(filters.FilterSet):
  price = filters.RangeFilter(field_name='price')
  address = filters.CharFilter(field_name='address', lookup_expr='icontains')

  class Meta:
    model = Advert
    fields = ['price', 'address']
