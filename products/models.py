from statistics import mode
from unicodedata import category
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from app.mixins.timestampable import TimestampableMixin
from app.mixins.status import StatusMixin
from app.mixins.str import StrMixin

class Product(TimestampableMixin, StatusMixin, StrMixin):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=3300)
    price = models.FloatField(null=False)
    qty = models.IntegerField(null=False)


class Category(TimestampableMixin, StatusMixin, StrMixin):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=3300)
