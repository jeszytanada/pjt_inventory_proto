from django.conf.urls import url, include
from . import views

app_name = 'pjt_inventory'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # List pjt_inventory/product_list
    url(r'^product_list', views.ProductListView.as_view(), name='product_list'),
    # List pjt_inventory/supplier_list
    url(r'^supplier_list', views.SupplierListView.as_view(), name='supplier_list'),
    # List pjt_inventory/brand_list
    url(r'^brand_list', views.BrandListView.as_view(), name='brand_list'),
    # List pjt_inventory/category_list
    url(r'^category_list', views.CategoryListView.as_view(), name='category_list'),
    # Details pjt_inventory/27/product_detail
    url(r'^(?P<pk>[0-9]+)/$', views.ProductDetailView.as_view(), name='product_detail'),
    # Details pjt_inventory/27/supplier_detail
    url(r'^(?P<pk>[0-9]+)/supplier_detail', views.SupplierDetailView.as_view(), name='supplier_detail'),
    # Details pjt_inventory/27/brand_detail
    url(r'^(?P<pk>[0-9]+)/brand_detail', views.BrandDetailView.as_view(), name='brand_detail'),
    # /pjt_inventory/product_add
    url(r'^product_add/$', views.ProductCreate.as_view(), name='product_add'),
    # /pjt_inventory/27/product_edit
    url(r'^(?P<pk>[0-9]+)/product_edit/$', views.ProductEdit.as_view(), name='product_edit'),
    # /pjt_inventory/27/product_delete
    url(r'^(?P<pk>[0-9]+)/product_delete/$', views.ProductDelete.as_view(), name='product_delete'),
    # /pjt_inventory/supplier_add
    url(r'^supplier_add/$', views.SupplierCreate.as_view(), name='supplier_add'),
    # /pjt_inventory/27/supplier_edit
    url(r'^(?P<pk>[0-9]+)/supplier_edit/$', views.SupplierEdit.as_view(), name='supplier_edit'),
    # /pjt_inventory/27/supplier_delete
    url(r'^(?P<pk>[0-9]+)/supplier_delete/$', views.SupplierDelete.as_view(), name='supplier_delete'),
    # /pjt_inventory/brand_add
    url(r'^brand_add/$', views.BrandCreate.as_view(), name='brand_add'),
    # /pjt_inventory/27/brand_edit
    url(r'^(?P<pk>[0-9]+)/brand_edit/$', views.BrandEdit.as_view(), name='brand_edit'),
    # /pjt_inventory/27/brand_delete
    url(r'^(?P<pk>[0-9]+)/brand_delete/$', views.BrandDelete.as_view(), name='brand_delete'),
    # List pjt_inventory/supplier_contact_list
    url(r'^(?P<pk>[0-9]+)/supplier_contact_list', views.SupplierContactListView.as_view(), name='supplier_contact_list'),
    # /pjt_inventory/supplier_contact_add
    url(r'^supplier_contact_add/$', views.SupplierContactCreate.as_view(), name='supplier_contact_add'),
    # /pjt_inventory/27/supplier_contact_edit
    url(r'^(?P<pk>[0-9]+)/supplier_contact_edit/$', views.SupplierContactEdit.as_view(), name='supplier_contact_edit'),
    # List pjt_inventory/27/category_product
    url(r'^(?P<pk>[0-9]+)/category_product', views.SubCategoryListView.as_view(), name='category_product'),
    # /pjt_inventory/category_add
    url(r'^category_add/$', views.CategoryCreate.as_view(), name='category_add'),
]