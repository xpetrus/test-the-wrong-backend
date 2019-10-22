from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def all_category_items(self):
        citems = Quote.objects.filter(category=self)
        allcitems = [item.id for item in citems]
        return allcitems


class Quote(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)
    quote = models.TextField(max_length=350)