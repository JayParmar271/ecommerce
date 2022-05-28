from django.db import models
from django.contrib.auth.models import User
from app.mixins.timestampable import TimestampableMixin
class Product(TimestampableMixin):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=3300)
    price = models.FloatField(null=False)
    qty = models.IntegerField(null=False)
