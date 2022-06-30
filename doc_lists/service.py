from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters

from .models import Doctor


class DoctorPagination(PageNumberPagination):
    page_size = 2
    max_page_size = 1000


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class DoctorFilter(filters.FilterSet):
    directions = CharFilterInFilter(field_name='directions__title', lookup_expr='in')
    years_of_experience = filters.RangeFilter()

    class Meta:
        model = Doctor
        fields = ['directions', 'years_of_experience']
