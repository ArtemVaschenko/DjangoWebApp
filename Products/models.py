from django.db import models

class Product(models.Model):
    mane = models.CharField(max_length=100)
    price =  models.IntegerField()