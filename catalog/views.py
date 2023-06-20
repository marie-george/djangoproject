from django.shortcuts import render
from django.views import generic

from catalog.models import Product


class IndexView(generic.TemplateView):
    template_name = 'catalog/home.html'
    extra_context = {
        'title': 'Главная страница',
        'object_list': Product.objects.all()[:4],
    }


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'User{name} with phone {phone} send message {message}')
    return render(request, 'catalog/contacts.html')


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