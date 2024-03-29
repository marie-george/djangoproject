from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Blog, Version, Category
from catalog.services import get_categories_from_cache


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

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related('version_set')
        queryset = queryset.filter(is_published=True)
        return queryset


class ProductDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_object()
        return context_data


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = Product
    permission_required = "catalog.add_product"
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = Product
    permission_required = "catalog.change_product"
    form_class = ProductForm
    template_name = 'catalog/product_form_with_formset.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user.groups.filter(name="Moderators"):
            kwargs['Moderator'] = True
        else:
            kwargs['Moderator'] = False
        # kwargs.update({'request': self.request})

        return kwargs

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise PermissionDenied()
        return self.object

    def get_success_url(self):
        return reverse('catalog:product_detail', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = Product
    permission_required = "catalog.delete_product"
    success_url = reverse_lazy('catalog:product_list')


class BlogListView(generic.ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(generic.DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_object()
        return context_data

    def get_object(self, **kwargs):
        views = super().get_object()
        views.increase_view_count()
        return views


class BlogCreateView(generic.CreateView):
    model = Blog
    fields = ('name', 'contents', 'preview')
    success_url = reverse_lazy('catalog:blog_list')


class BlogUpdateView(generic.UpdateView):
    model = Blog
    fields = ('name', 'contents', 'preview')

    def get_success_url(self):
        return reverse('catalog:blog_detail', kwargs={'slug': self.object.slug})


class BlogDeleteView(generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')


def toggle_publication(request, slug):
    post_item = get_object_or_404(Blog, slug=slug)
    if post_item.is_published:
        post_item.is_published = False
    else:
        post_item.is_published = True

    post_item.save()

    return redirect(reverse('catalog:blog_detail', args=[post_item.slug]))


@permission_required("catalog.can_cancell_publication")
def toggle_publication_product(request, slug):
    post_item = get_object_or_404(Product, slug=slug)
    if post_item.is_published:
        post_item.is_published = False
    else:
        post_item.is_published = True

    post_item.save()

    return redirect(reverse('catalog:product_detail', args=[post_item.slug]))


class CategoriesListView(generic.ListView):
    model = Category
    extra_context = {
        'title': 'Список категорий',
        'category_list': get_categories_from_cache()
    }