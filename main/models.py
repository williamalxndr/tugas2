from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField()
    price = models.IntegerField()
    description = models.TextField()
    