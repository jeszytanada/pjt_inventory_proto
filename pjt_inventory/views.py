#from django.shortcuts import render
#from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .forms import ProductForm, SupplierForm, BrandForm, SupplierContactForm, CategoryForm
from .models import Product, Supplier, Brand, SupplierContact, CategoryDescription, Category

class IndexView(TemplateView):
    template_name = "pjt_inventory/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['latest_product'] = Product.objects.all()[:1]
        return context

'''
    PRODUCTS
'''
class ProductListView(ListView):
    template_name = 'pjt_inventory/product_list.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailView(DetailView):
    model = Product
    template_name = 'pjt_inventory/product_detail.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'pjt_inventory/product_detail.html'


class ProductCreate(CreateView):
    model = Product
    template_name = 'pjt_inventory/product_add.html'
    form_class = ProductForm
    success_url = reverse_lazy('pjt_inventory:product_list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            instance = form.instance
            instance.modified_by = self.request.user
            instance.save()
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
            instance = form_class.instance
            instance.modified_by = self.request.user
            instance.save()
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

'''
    SUPPLIERS
'''
class SupplierListView(ListView):
    template_name = 'pjt_inventory/supplier_list.html'
    context_object_name = 'supplier_list'

    def get_queryset(self):
        return Supplier.objects.all()


class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'pjt_inventory/supplier_detail.html'


class SupplierEdit(UpdateView):
    model = Supplier
    template_name = 'pjt_inventory/supplier_edit.html'
    form_class = SupplierForm
    success_url = reverse_lazy('pjt_inventory:supplier_list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            instance = form.instance
            instance.modified_by = self.request.user
            instance.save()
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


class SupplierCreate(CreateView):
    model = Supplier
    template_name = 'pjt_inventory/supplier_add.html'
    form_class = SupplierForm
    success_url = reverse_lazy('pjt_inventory:supplier_list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            instance = form.instance
            instance.modified_by = self.request.user
            instance.save()
            return super(SupplierCreate, self).form_valid(form)
        else:
            form = SupplierForm()
            return render(self, 'pjt_inventory/supplier_add.html', {'form': form})

'''
    SUPPLIER CONTACTS
'''
class SupplierContactListView(ListView):
    template_name = 'pjt_inventory/supplier_contact_list.html'
    context_object_name = 'supplier_contact_list'

    def get_queryset(self):
        supplier = Supplier.objects.get(pk=self.kwargs.get('pk'))
        return supplier.supplier_contacts.all()


class SupplierContactCreate(CreateView):
    model = SupplierContact
    template_name = 'pjt_inventory/supplier_contact_add.html'
    form_class = SupplierContactForm
    success_url = reverse_lazy('pjt_inventory:supplier_list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            instance = form.instance
            instance.modified_by = self.request.user
            instance.save()
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
            instance = form.instance
            instance.modified_by = self.request.user
            instance.save()
            return super(SupplierContactEdit, self).form_valid(form)
        else:
            form = SupplierContactForm()
            return render(self, 'pjt_inventory/supplier_contact_edit.html', {'form': form})

'''
    BRANDS
'''
class BrandListView(ListView):
    template_name = 'pjt_inventory/brand_list.html'
    context_object_name = 'brand_list'

    def get_queryset(self):
        return Brand.objects.all()


class BrandDetailView(DetailView):
    model = Brand
    template_name = 'pjt_inventory/brand_detail.html'


class BrandCreate(CreateView):
    model = Brand
    template_name = 'pjt_inventory/brand_add.html'
    form_class = BrandForm
    success_url = reverse_lazy('pjt_inventory:brand_list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            instance = form.instance
            instance.modified_by = self.request.user
            instance.save()
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
            instance = form.instance
            instance.modified_by = self.request.user
            instance.save()
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

'''
    CATEGORY
'''

class CategoryListView(ListView):
    template_name = 'pjt_inventory/category_list.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        #return Category.objects.filter(is_child=False).exclude(id=11)
        return Category.objects.filter(parent_id=11).exclude(id=11)


class CategorySubListView(ListView):
    template_name = 'pjt_inventory/category_sub_list.html'
    context_object_name = 'category_sub_list'

    def get_queryset(self):
        return Category.objects.filter(parent_id=self.kwargs.get('pk'))

    def get_context_data(self, *args, **kwargs):
        context = super(CategorySubListView, self).get_context_data(*args, **kwargs)
        context['category_products'] = Product.objects.filter(category=self.kwargs.get('pk'))
        return context


class CategoryProductListView(ListView):
    template_name = 'pjt_inventory/category_product.html'
    context_object_name = 'category_products'

    def get_queryset(self):
        return Product.objects.filter(category=self.kwargs.get('pk'))

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryProductListView, self).get_context_data(*args, **kwargs)
        context['category_sub_list'] = Category.objects.filter(parent_id=self.kwargs.get('pk'))
        return context


class CategoryCreate(CreateView):
    model = Category
    template_name = 'pjt_inventory/category_add.html'
    form_class = CategoryForm
    success_url = reverse_lazy('pjt_inventory:category_list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            instance = form.instance
            instance.modified_by = self.request.user
            instance.save()
            return super(CategoryCreate, self).form_valid(form)
        else:
            form = CategoryForm()
            return render(self, 'pjt_inventory/category_add.html', {'form': form})


class CategoryEdit(UpdateView):
    model = Category
    template_name = 'pjt_inventory/category_edit.html'
    form_class = CategoryForm
    success_url = reverse_lazy('pjt_inventory:category_list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            instance = form.instance
            instance.modified_by = self.request.user
            instance.save()
            return super(CategoryEdit, self).form_valid(form)
        else:
            form = CategoryForm()
            return render(self, 'pjt_inventory/category_edit.html', {'form': form})
'''
    SUBCATEGORY

class SubCategoryListView(ListView):
    template_name = 'pjt_inventory/category_product.html'
    context_object_name = 'sub_category_list'

    def get_queryset(self):
        subcat = Category.objects.get(pk=self.kwargs.get('pk'))
        return subcat.parent.all()

class SubCategoryProductsView(ListView):
    template_name = 'pjt_inventory/category_product.html'
    context_object_name = 'sub_category_products'

    def get_queryset(self):
        subcat = Category.objects.get(pk=self.kwargs.get('pk'))
        return subcat.parent.all()
'''