from django.db import models
from django.utils import timezone
#from .models import Brand, Supplier
import datetime

class Supplier(models.Model):
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True, null=True)
    tax_num = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=False, default='000-0000')
    fax = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True)
    zipcode = models.CharField(max_length=10, null=True)
    image = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)
    tags = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(choices=BOOL_CHOICES, default=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    modified_by = models.ForeignKey('auth.User', null=True)

    def __str__(self):
        return self.name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Supplier._meta.fields]

class Brand(models.Model):
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

    name = models.CharField(max_length=100)
    desc = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)
    tags = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(choices=BOOL_CHOICES, default=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    modified_by = models.ForeignKey('auth.User', null=True)

    def __str__(self):
        return self.name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Brand._meta.fields]

class Category(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    tags = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    modified_by = models.ForeignKey('auth.User', null=True)

    def __str__(self):
        return self.name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Category._meta.fields]

class SubCategory(models.Model):
    parent_name = models.CharField(max_length=100, blank=True)
    parent_category = models.ForeignKey(Category, related_name='parent', on_delete=models.SET_NULL, null=True)
    child_name = models.CharField(max_length=100, blank=True)
    child_category = models.ForeignKey(Category, related_name='children', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.parent_name

class Product(models.Model):
    BOOL_CHOICES = ((True, 'active'), (False, 'inactive'))
    REGULAR = 'RE'
    SAMPLE = 'SA'
    TESTER = 'TE'
    OTHERS = 'OT'

    SIZE_FLAG_CHOICES = (
        (REGULAR, 'Regular'),
        (SAMPLE, 'Sample'),
        (TESTER, 'Tester'),
        (OTHERS, 'Others'),
    )

    ALWAYS = 'Always'
    NORMAL = 'Normal'
    SPECIAL = 'Special'
    FREE_SHIPPING_CHOICES = (
        (ALWAYS, 'Always'),
        (NORMAL, 'Normal'),
        (SPECIAL, 'Special')
    )
    barcode = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, related_name='brands', on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(Supplier, related_name='suppliers', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.SET_NULL, null=True)
    #sub_category = models.ForeignKey(Category, related_name='sub_categories', on_delete=models.SET_NULL, null=True)
    size_flag = models.CharField(max_length=2, choices=SIZE_FLAG_CHOICES, default=REGULAR)
    price_cost = models.FloatField(default=0)
    price_bought = models.FloatField(default=0)
    price_wholesale = models.FloatField(default=0)
    price_retail = models.FloatField(default=0)
    free_shipping = models.CharField(max_length=7, choices=FREE_SHIPPING_CHOICES, null=True)
    order_min = models.IntegerField(default=1)
    order_max = models.IntegerField(default=1)
    desc_header = models.CharField(max_length=100, blank=True)
    desc_body = models.TextField(blank=True)
    status = models.BooleanField(choices=BOOL_CHOICES, default=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    tags = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    date_publish = models.DateTimeField(blank=True, null=True)
    modified_by = models.ForeignKey('auth.User', null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Product._meta.fields]

class SupplierContact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, related_name='supplier_contacts', on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    notes = models.TextField(null=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    modified_by = models.ForeignKey('auth.User', null=True)

    def __str__(self):
        return self.first_name