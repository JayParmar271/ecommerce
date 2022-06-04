from django.contrib import admin
from .models import Product, Category, Image

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'category', 'price', 'qty', 'is_active', 'created')
    exclude = ('user',)

    class ImageInline(admin.TabularInline):
        model = Image

    inlines = [ImageInline,]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)

    @admin.action(description='Mark selected product to active')
    def mark_to_active(modeladmin, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description='Mark selected product to inactive')
    def mark_to_inactive(modeladmin, request, queryset):
        queryset.update(is_active=False)

    actions = [mark_to_active, mark_to_inactive]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)