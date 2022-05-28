from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'category', 'price', 'qty', 'is_active', 'created')
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)