from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'qty', 'is_active', 'created')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)