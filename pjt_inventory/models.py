from django.db import models
from django.utils import timezone
# Create your models here.

class Product(models.Model):
    # models.ForeignKey('auth.User')
    #id = models.ForeignKey(ForeignKey=True)
    name = models.TextField()
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
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

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Product._meta.fields]