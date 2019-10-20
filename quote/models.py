from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)


class Quote(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)
    quote = models.TextField(max_length=350)