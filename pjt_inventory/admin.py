from django.contrib import admin
from .models import Product, Supplier, Brand, SupplierContact, Category, CategoryDescription, ProductAttribute
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Created', {'fields': ['date_created'], 'classes': ['collapse']}),
        ('Publish Date', {'fields': ['date_publish'], 'classes': ['collapse']}),
        ('Other properties', {
            'classes': ('collapse',),
            'fields': ('barcode','brand','supplier','category','size_flag','price_cost','price_bought','price_wholesale','price_retail',
                       'free_shipping','order_min','order_max','desc_header','desc_body','image','remarks','tags','status','date_updated','modified_by'),
        }),
    ]

class SupplierAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['supplier_name']}),
        ('Person', {'fields': ['supplier_contact_person'], 'classes': ['collapse']}),
        ('Other INFO', {
            'classes': ('collapse',),
            'fields': ('supplier_contact','email','created_date','updated_date','modified_by'),
        }),
    ]

admin.site.register(Product, ProductAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Brand)
admin.site.register(SupplierContact)
admin.site.register(Category)
admin.site.register(CategoryDescription)
admin.site.register(ProductAttribute)