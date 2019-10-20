from rest_framework import serializers
from .models import Category, Quote


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = 'name'


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quote
        fields = ('category', 'quote')
