from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Product, Supplier, Brand, SupplierContact, Category, SubCategory
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .forms import ProductForm, SupplierForm, BrandForm, SupplierContactForm, CategoryForm

# Create your views here.
class IndexView(TemplateView):
    template_name = "pjt_inventory/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['latest_product'] = Product.objects.all()[:1]
        return context

class ProductListView(ListView):
    template_name = 'pjt_inventory/product_list.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.all()

class SupplierListView(ListView):
    template_name = 'pjt_inventory/supplier_list.html'
    context_object_name = 'supplier_list'

    def get_queryset(self):
        return Supplier.objects.all()

class BrandListView(ListView):
    template_name = 'pjt_inventory/brand_list.html'
    context_object_name = 'brand_list'

    def get_queryset(self):
        return Brand.objects.all()

class CategoryListView(ListView):
    template_name = 'pjt_inventory/category_list.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        #return Category.objects.all()
        # category = Category.objects.get(pk=self.kwargs.get('pk'))
        #parents_id = SubCategory.objects.values_list('parent_category', flat=True)
        #categories = Category.objects.filter(pk__in=parents_id)
        #no_child_categories = Category.objects.filter(pk__in=parents_id)
        #parents_list = categories + no_child_categories
        children_id = SubCategory.objects.values_list('child_category', flat=True)
        categories = Category.objects.exclude(pk__in=children_id)
        return categories

# Get all the child id
class SubCategoryListView(ListView):
    template_name = 'pjt_inventory/category_product.html'
    context_object_name = 'sub_category_list'

    def get_queryset(self):
        subcat = Category.objects.get(pk=self.kwargs.get('pk'))
        return subcat.parent.all()

class ProductDetailView(DetailView):
    model = Product
    template_name = 'pjt_inventory/product_detail.html'

class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'pjt_inventory/supplier_detail.html'

class BrandDetailView(DetailView):
    model = Brand
    template_name = 'pjt_inventory/brand_detail.html'

class ProductCreate(CreateView):
    model = Product
    template_name = 'pjt_inventory/product_add.html'
    form_class = ProductForm
    success_url = reverse_lazy('pjt_inventory:product_list')

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
    success_url = reverse_lazy('pjt_inventory:product_list')

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

class SupplierCreate(CreateView):
    model = Supplier
    template_name = 'pjt_inventory/supplier_add.html'
    form_class = SupplierForm
    success_url = reverse_lazy('pjt_inventory:supplier_list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return super(SupplierCreate, self).form_valid(form)
        else:
            form = SupplierForm()
            return render(self, 'pjt_inventory/supplier_add.html', {'form': form})

class SupplierEdit(UpdateView):
    model = Supplier
    template_name = 'pjt_inventory/supplier_edit.html'
    form_class = SupplierForm
    success_url = reverse_lazy('pjt_inventory:supplier_list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return super(SupplierEdit, self).form_valid(form)
        else:
            form = SupplierForm()
            return render(self, 'pjt_inventory/supplier_edit.html', {'form': form})

class SupplierDelete(DeleteView):
    model = Supplier
    template_name = 'pjt_inventory/supplier_delete.html'
    success_url = reverse_lazy('pjt_inventory:supplier_list')

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

class BrandCreate(CreateView):
    model = Brand
    template_name = 'pjt_inventory/brand_add.html'
    form_class = BrandForm
    success_url = reverse_lazy('pjt_inventory:brand_list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return super(BrandCreate, self).form_valid(form)
        else:
            form = BrandForm()
            return render(self, 'pjt_inventory/brand_add.html', {'form': form})

class BrandEdit(UpdateView):
    model = Brand
    template_name = 'pjt_inventory/brand_edit.html'
    form_class = BrandForm
    success_url = reverse_lazy('pjt_inventory:brand_list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return super(BrandEdit, self).form_valid(form)
        else:
            form = BrandForm()
            return render(self, 'pjt_inventory/brand_edit.html', {'form': form})

class BrandDelete(DeleteView):
    model = Brand
    template_name = 'pjt_inventory/brand_delete.html'
    success_url = reverse_lazy('pjt_inventory:brand_list')

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

class SupplierContactListView(ListView):
    template_name = 'pjt_inventory/supplier_contact_list.html'
    context_object_name = 'supplier_contact_list'

    def get_queryset(self):
        supplier = Supplier.objects.get(pk=self.kwargs.get('pk'))
        return supplier.supplier_contacts.all()

class CategoryProductListView(ListView):
    template_name = 'pjt_inventory/category_product.html'
    context_object_name = 'category_product_list'

    def get_queryset(self):
        category = Category.objects.get(pk=self.kwargs.get('pk'))
        return category.categories.all()

class SupplierContactCreate(CreateView):
    model = SupplierContact
    template_name = 'pjt_inventory/supplier_contact_add.html'
    form_class = SupplierContactForm
    success_url = reverse_lazy('pjt_inventory:supplier_list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return super(SupplierContactCreate, self).form_valid(form)
        else:
            form = SupplierContactForm()
            return render(self, 'pjt_inventory/supplier_contact_add.html', {'form': form})

class SupplierContactEdit(UpdateView):
    model = SupplierContact
    template_name = 'pjt_inventory/supplier_contact_edit.html'
    form_class = SupplierContactForm
    success_url = reverse_lazy('pjt_inventory:supplier_list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return super(SupplierContactEdit, self).form_valid(form)
        else:
            form = SupplierContactForm()
            return render(self, 'pjt_inventory/supplier_contact_edit.html', {'form': form})

class CategoryCreate(CreateView):
    model = Category
    template_name = 'pjt_inventory/category_add.html'
    form_class = CategoryForm
    success_url = reverse_lazy('pjt_inventory:category_list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return super(CategoryCreate, self).form_valid(form)
        else:
            form = CategoryForm()
            return render(self, 'pjt_inventory/category_add.html', {'form': form})