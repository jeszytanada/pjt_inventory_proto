from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Product
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ProductForm

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
    template_name = 'pjt_inventory/product_list.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.all()

class ProductCreate(CreateView):
    model = Product
    template_name = 'pjt_inventory/product_add.html'
    form_class = ProductForm
    success_url = reverse_lazy('pjt_inventory:index')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return super(ProductCreate, self).form_valid(form)
        else:
            form = ProductForm()
            return render(self, 'pjt_inventory/product_add.html', {'form': form})

class ProductEdit(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'pjt_inventory/product_edit.html'
    success_url = reverse_lazy('pjt_inventory:index')

    def form_valid(self, form_class):
        if form_class.is_valid():
            form_class.save()
            return super(ProductEdit, self).form_valid(form_class)
        else:
            form = ProductForm()
            return render(self, 'pjt_inventory/product_edit.html', {'form': form})

class ProductDelete(DeleteView):
    model = Product
    template_name = 'pjt_inventory/product_delete.html'
    success_url = reverse_lazy('pjt_inventory:index')

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)