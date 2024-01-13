from rest_framework import serializers
from .models import Tusks
from users.models import News

class TusksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tusks
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
    