from django.db import models
from django.utils import timezone

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

class CategoryDescription(models.Model):
    categories_name = models.CharField(max_length=100)
    categories_description = models.TextField(null=True, blank=True)
    tags = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    modified_by = models.ForeignKey('auth.User', null=True)

    def __str__(self):
        return self.categories_name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in CategoryDescription._meta.fields]

class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, blank=True)
    is_child = models.BooleanField(default=False)
    parent = models.ForeignKey("self", default=11)
    image = models.TextField(null=True, blank=True)
    tags = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    modified_by = models.ForeignKey('auth.User', null=True)
    #parent = models.ForeignKey(CategoryDescription, related_name='prime_category', default=0)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Category._meta.fields]

class Product(models.Model):
    BOOL_CHOICES = ((True, 'active'), (False, 'inactive'))
    REGULAR = 'Regular'
    SAMPLE = 'Sample'
    TESTER = 'Tester'
    OTHERS = 'Others'

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
    size_flag = models.CharField(max_length=7, choices=SIZE_FLAG_CHOICES, default=REGULAR)
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

class ProductAttribute(models.Model):
    COLOR = 'Color'
    SIZE = 'Size'
    WEIGHT = 'Weight'
    TYPE_CHOICES = (
        (COLOR, 'Color'),
        (SIZE, 'Size'),
        (WEIGHT, 'Weight')
    )
    product = models.ForeignKey(Product, related_name='product_attr', on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES, default=COLOR)
    value = models.CharField(max_length=80)

    def __str__(self):
        return self.product_attr.name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in ProductAttribute._meta.fields]


class ProductStock(models.Model):
    product = models.ForeignKey(Product, related_name='product_stock', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    date_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product_stock.name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in ProductStock._meta.fields]


class ProductStockHistory(models.Model):
    product = models.ForeignKey(Product, related_name='product_stock_history', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    type = models.IntegerField(default=0)
    reference_type = models.IntegerField(default=0)
    reference_id = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product_stock.name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in ProductStockHistory._meta.fields]