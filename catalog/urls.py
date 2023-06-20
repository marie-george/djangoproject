from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import IndexView, contacts, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_item/<int:pk>', ProductDetailView.as_view(), name='product_item'),
]