from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, product_list, product_item

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product_list/', product_list, name='product_list'),
    path('product_item/<int:pk>', product_item, name='product_item'),
]