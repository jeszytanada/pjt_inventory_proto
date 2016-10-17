from django import forms
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User
from .models import Product, Supplier, Brand, SupplierContact, CategoryDescription, Category

class ProductForm(forms.ModelForm):
    #pub_date = forms.DateField(initial=timezone.now())
    #end_date = forms.DateField(initial=timezone.now() + timezone.timedelta(days=1))
    class Meta:
        model = Product
        exclude = ('id',)
        fields = ['barcode','name','brand','supplier','category','size_flag','price_cost','price_bought','price_wholesale','price_retail',
                  'free_shipping','order_min','order_max','desc_header','desc_body','image','remarks','tags','status','date_publish']

    def clean(self):
        cleaned_data = super(ProductForm, self).clean()
        return cleaned_data
        # pub_date = cleaned_data.get('pub_date')
        # end_date = cleaned_data.get('end_date')
        # if pub_date and end_date:
        #     if pub_date < date.today() or end_date <= date.today():
        #         msg = "Date cannot be in the past!"
        #         self.add_error('pub_date', msg)
        #         self.add_error('end_date', msg)
        #     elif end_date <= pub_date:
        #         msg = "End Date cannot be older or same than the opening date.."
        #         self.add_error('end_date', msg)

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        widgets = {
            'is_active': forms.RadioSelect
        }
        exclude = ('id',)
        fields = ['name','desc','tax_num','phone','fax','email','address','city','state','country','zipcode','image','url','tags','is_active']

    def clean(self):
        cleaned_data = super(SupplierForm, self).clean()
        return cleaned_data

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        widgets = {
            'is_active': forms.RadioSelect
        }
        exclude = ('id',)
        fields = ['name','desc','image','url','tags','is_active']

    def clean(self):
        cleaned_data = super(BrandForm, self).clean()
        return cleaned_data

class SupplierContactForm(forms.ModelForm):
    class Meta:
        model = SupplierContact
        exclude = ('id',)
        fields = ['first_name','last_name','supplier','email','phone','fax','mobile','dept','notes']

    def clean(self):
        cleaned_data = super(SupplierContactForm, self).clean()
        return cleaned_data

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('id',)
        #fields = ['categories_name','categories_description','tags','date_created','date_updated','modified_by']
        fields = ['name', 'description', 'is_child', 'parent', 'image', 'tags']

    def clean(self):
        cleaned_data = super(CategoryForm, self).clean()
        return cleaned_data