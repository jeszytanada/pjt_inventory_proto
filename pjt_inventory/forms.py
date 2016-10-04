from django import forms
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User
from .models import Product

class ProductForm(forms.ModelForm):
    #pub_date = forms.DateField(initial=timezone.now())
    #end_date = forms.DateField(initial=timezone.now() + timezone.timedelta(days=1))
    class Meta:
        model = Product
        exclude = ('id',)
        fields = ['name', 'barcode', 'size', 'color', 'quantity', 'manufacturer', 'brand', 'retail_price', 'wholesale_price', 'weight', 'description']

    def clean(self):
        cleaned_data = super(ProductForm, self).clean()
        pub_date = cleaned_data.get('pub_date')
        end_date = cleaned_data.get('end_date')
        if pub_date and end_date:
            if pub_date < date.today() or end_date <= date.today():
                msg = "Date cannot be in the past!"
                self.add_error('pub_date', msg)
                self.add_error('end_date', msg)
            elif end_date <= pub_date:
                msg = "End Date cannot be older or same than the opening date.."
                self.add_error('end_date', msg)
        return cleaned_data