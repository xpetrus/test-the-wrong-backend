from rest_framework import serializers
from .models import Category, Quote


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'all_category_items')



class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quote
        fields = ('category', 'quote')
