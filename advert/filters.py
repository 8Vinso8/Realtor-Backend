from django_filters import rest_framework as filters
from advert.models import Advert

class AdvertFilter(filters.FilterSet):
  price = filters.RangeFilter(field_name='price')
  address = filters.CharFilter(field_name='address', lookup_expr='icontains')
  city = filters.CharFilter(field_name='city', lookup_expr='icontains')
  street = filters.CharFilter(field_name='street', lookup_expr='icontains')
  advert_type = filters.CharFilter(field_name='advert_type', lookup_expr='exact')
  floor = filters.NumberFilter(field_name='floor', lookup_expr='exact')
  is_sold = filters.BooleanFilter(field_name='sold', lookup_expr='exact')

  class Meta:
    model = Advert
    fields = ['price', 'address', 'city', 'street', 'advert_type', 'floor', 'is_sold']
