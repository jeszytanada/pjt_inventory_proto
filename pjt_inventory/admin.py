from django.contrib import admin
from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Created', {'fields': ['created_date'], 'classes': ['collapse']}),
        ('Publish Date', {'fields': ['published_date'], 'classes': ['collapse']}),
        ('Other properties', {
            'classes': ('collapse',),
            'fields': ('size', 'color', 'quantity', 'manufacturer', 'brand', 'barcode',
                       'retail_price', 'wholesale_price', 'weight', 'description',
                       'created_date', 'updated_date'),
        }),
    ]

admin.site.register(Product, ProductAdmin)