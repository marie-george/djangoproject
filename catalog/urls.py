from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import IndexView, ContactsView, ProductListView, ProductDetailView, BlogListView, BlogDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_item/<int:pk>', ProductDetailView.as_view(), name='product_item'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_detail/<int:pk>', BlogDetailView.as_view(), name='product_item')
]