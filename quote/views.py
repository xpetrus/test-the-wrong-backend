from django.shortcuts import render
from rest_framework import viewsets  # allows them datas to been seen when that specific route is called...
from .models import Quote, Category
from .serializers import CategorySerializer, QuoteSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

