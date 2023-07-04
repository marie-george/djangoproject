from django.contrib import admin

from catalog.models import Product, Category, Blog, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    search_fields = ('name', 'description')
    list_filter = ('author',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Version)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'version_name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'contents')
    search_fields = ('name', 'contents')
    list_filter = ('contents',)
    prepopulated_fields = {"slug": ("name",)}