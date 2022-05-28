from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'qty', 'description', 'created')

admin.site.register(Product, ProductAdmin)
