from django.db import models
import uuid
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    ratings = models.FloatField()
    category_choices = [
        ("elektronik", "Elektronik"),
        ("fashion", "Fashion & Style"), 
        ("makanan", "Makanan & Minuman"),
        ("furniture", "Furniture"),
        ("otomotif", "Otomotif"),
        ("alattulis", "Alat Tulis"),
        ("others", "Others")
    ]
    category = models.CharField(max_length=20, choices=category_choices)

    @property
    def is_available(self):
        return self.stock > 0
    


