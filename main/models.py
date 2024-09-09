from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    ratings = models.FloatField()

    @property
    def is_available(self):
        return self.stock > 0
    
