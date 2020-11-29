from django.db import models

# Create your models here.


class Product(models.Model):
    item = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    price = models.CharField(max_length=200)

    def __str__(self):
        return self.item
