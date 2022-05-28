from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=30)
    price = models.FloatField(null=False)
    qty = models.IntegerField(null=False)
