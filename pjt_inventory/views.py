from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView

# Create your views here.
class IndexView(ListView):
    template_name = 'pjt_inventory/index.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.all()

class DetailView(DetailView):
    model = Product
    template_name = 'pjt_inventory/detail.html'

class ProductListView(ListView):
    model = Product
    template_name = 'pjt_inventory/product_list.html'