from rest_framework.filters import BaseFilterBackend
import coreapi

import django_filters
from .models import ProgrammingLanguage

class ProgrammingLanguageFilter(django_filters.FilterSet):
    def get_filters(self, request, view):
        fields = [
            coreapi.Field(
                name='name',
                location='query',
                required=False,
                type='string',
                description='Filter by topic name',
            )
        ]
        return fields

    def filter_queryset(self, request, queryset, view):
        name = request.query_params.get('name')
        if name:
            return queryset.filter(topic_name__icontains=name)
        return queryset


class ProgrammingLanguageFilterSet(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    creation_time = django_filters.DateTimeFilter(field_name='creation_time')
    author = django_filters.CharFilter(field_name='author')
    logo = django_filters.CharFilter(field_name='logo')
    detailed_information = django_filters.CharFilter(field_name='detailed_information')

    class Meta:
        model = ProgrammingLanguage
        fields = ['name', 'creation_time', 'author', 'logo', 'detailed_information']


class PyTopicFilter(django_filters.FilterSet):
    topic_name = django_filters.CharFilter(lookup_expr='icontains')
    topic_subject = django_filters.CharFilter(lookup_expr='icontains')
    topic_content = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Topic
        fields = ['topic_name', 'topic_subject', 'topic_content']
