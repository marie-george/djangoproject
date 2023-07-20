from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import IndexView, ContactsView, ProductListView, ProductDetailView, BlogListView, BlogDetailView, \
    BlogCreateView, BlogUpdateView, BlogDeleteView, toggle_publication, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, toggle_publication_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_detail/<slug:slug>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_detail/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/update/<slug:slug>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<slug:slug>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog/toggle/<slug:slug>/', toggle_publication, name='toggle_publication'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/update/<slug:slug>/', ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<slug:slug>/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/toggle/<slug:slug>/', toggle_publication_product, name='toggle_publication_product'),
]