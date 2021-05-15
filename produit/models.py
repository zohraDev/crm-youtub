from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Produit(models.Model):
    name = models.CharField(max_length=20, null=True)
    price = models.FloatField(null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
