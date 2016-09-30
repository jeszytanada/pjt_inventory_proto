from django.conf.urls import url, include
from . import views

app_name = 'pjt_inventory'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # Details pjt_inventory/27/detail
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # Details pjt_inventory/27/list
    url(r'^(?P<pk>[0-9]+)/list', views.ListView.as_view(), name='list'),
]