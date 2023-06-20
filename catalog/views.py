from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from catalog.models import Product, Blog


class IndexView(generic.TemplateView):
    template_name = 'catalog/home.html'
    extra_context = {
        'title': 'Главная страница',
        'object_list': Product.objects.all()[:4],
    }


class ContactsView(generic.TemplateView):
    template_name = 'catalog/contacts.html'


class ProductListView(generic.ListView):
    model = Product
    extra_context = {
        'title': 'Каталог товаров',
    }


class ProductDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_object()
        return context_data


class BlogListView(generic.ListView):
    model = Blog


class BlogDetailView(generic.DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_object()
        return context_data


class BlogCreateView(generic.CreateView):
    model = Blog
    fields = ('name', 'contents', 'preview')
    success_url = reverse_lazy('catalogue:blog_list')


class BlogUpdateView(generic.UpdateView):
    model = Blog
    fields = ('name', 'contents', 'preview')
    success_url = reverse_lazy('catalogue:blog_list')


class BlogDeleteView(generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('catalogue:blog_list')