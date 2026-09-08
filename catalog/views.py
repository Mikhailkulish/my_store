from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product


def home(request):
    products = Product.objects.all()
    context = {"products": products}

    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено. Мы свяжемся с Вами по номеру {phone}")
    return render(request, 'catalog/contacts.html')


def product_detail(request, id_product):
    product = Product.objects.get(id=id_product)
    context = {
        'product_name': product.name,
        'product_description': product.description,
        'product_photo': product.photo.url,
        'product_category': product.category,
        'product_price': product.price,
        'product_created_at': product.created_at,
        'product_updated_at': product.updated_at
    }

    return render(request, 'catalog/product_detail.html', context)
