from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = (
        "name",
        "description",
        "photo",
        "category",
        "price"
    )
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = (
        "name",
        "description",
        "photo",
        "category",
        "price"
    )
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#
#         return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено. Мы свяжемся с Вами по номеру {phone}")
#     return render(request, 'catalog/contacts.html')

class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        context['phone'] = '+7 (999) 999-99-99'
        context['email'] = 'info@mystore.ru'
        context['address'] = 'г. Москва, Красная площадь, ГУМ'
        return context
