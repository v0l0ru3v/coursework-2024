from rest_framework import serializers
from .models import Tusks
from users.models import News
import django_filters

class TusksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tusks
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class TusksFilter(django_filters.FilterSet):
    title__icontains = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    class Meta:
        model = Tusks
        fields = ['title__icontains']

    