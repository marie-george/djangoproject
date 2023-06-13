from django.shortcuts import render

from catalog.models import Product


def index(request):
    context = {'object_list': Product.objects.all()[:4], 'title': 'Каталог товаров'}
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'User{name} with phone {phone} send message {message}')
    return render(request, 'catalog/contacts.html')


def product_list(request):
    products = Product.objects.all()
    context = {
        'object_list': products,
        'title': 'Каталог товаров',
    }
    return render(request, 'catalog/product_list.html', context)

def product_item(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object': product_item,
        'title': f'{product_item.author} {product_item.name}',
    }
    return render(request, 'catalog/product_item.html', context)