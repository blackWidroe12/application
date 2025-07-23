import django_filters
from django_filters import rest_framework as filters
from infrastructure.models.spatial import Infrastructure
from infrastructure.models.core import Ward

class InfrastructureFilter(filters.FilterSet):
    ward = django_filters.NumberFilter(field_name='ward__id')
    type = django_filters.CharFilter(field_name='type__name')
    status = django_filters.CharFilter(field_name='status')
    bbox = django_filters.CharFilter(method='filter_bbox')

    class Meta:
        model = Infrastructure
        fields = ['ward', 'type', 'status']

    def filter_bbox(self, queryset, name, value):
        try:
            from django.contrib.gis.geos import Polygon
            minx, miny, maxx, maxy = map(float, value.split(','))
            bbox = Polygon.from_bbox((minx, miny, maxx, maxy))
            return queryset.filter(geom__within=bbox)
        except (ValueError, TypeError):
            return queryset

class WardFilter(filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    code = django_filters.CharFilter(lookup_expr='iexact')
    population_min = django_filters.NumberFilter(field_name='population', lookup_expr='gte')
    population_max = django_filters.NumberFilter(field_name='population', lookup_expr='lte')

    class Meta:
        model = Ward
        fields = ['name', 'code', 'population_min', 'population_max']