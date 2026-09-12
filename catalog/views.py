from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


# def home(request):
#     products = Product.objects.all()
#     context = {"products": products}
#
#     return render(request, 'catalog/home.html', context)
#

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено. Мы свяжемся с Вами по номеру {phone}")
    return render(request, 'catalog/contacts.html')


# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#
#     return render(request, 'catalog/product_detail.html', context)
