from django.contrib.auth.models import User
from django.db import models

from Products.models import Product


# Create your models here.
class SalesOrger(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ManyToManyField(Product)