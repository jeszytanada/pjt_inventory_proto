from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Product(models.Model):
    # models.ForeignKey('auth.User')
    name = models.TextField()
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    variant = models.CharField(max_length=100, default='')
    quantity = models.IntegerField()
    manufacturer = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    barcode = models.CharField(max_length=100)
    retail_price = models.BigIntegerField()
    wholesale_price = models.BigIntegerField()
    weight = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    modified_by = models.ForeignKey('auth.User', null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Product._meta.fields]

class Supplier(models.Model):
    #product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier_name = models.CharField(max_length=100)
    supplier_contact_person = models.CharField(max_length=100)
    supplier_contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    modified_by = models.ForeignKey('auth.User', null=True)

    def __str__(self):
        return self.supplier_name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Supplier._meta.fields]