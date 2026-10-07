from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.forms import ProductForm
from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if product.owner != request.user and not request.user.has_perm('catalog.can_delete_any_product'):
            messages.error(request, 'Вы можете редактировать только свои товары')
            return redirect('catalog:product_list')
        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if product.owner != request.user and not request.user.has_perm('catalog.can_delete_any_product'):
            messages.error(request, 'Недостаточно прав для удаления товара')
            return redirect('catalog:product_list')
        return super().dispatch(request, *args, **kwargs)


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        context['phone'] = '+7 (999) 999-99-99'
        context['email'] = 'info@mystore.ru'
        context['address'] = 'г. Москва, Красная площадь, ГУМ'
        return context


class ProductPublishView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'catalog.can_publish_product'
    raise_exception = True

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.is_published = True
        product.save(update_fields=['is_published'])
        return redirect('catalog:product_detail', pk=product.pk)


class ProductUnpublishView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'catalog.can_unpublish_product'
    raise_exception = True

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.is_published = False
        product.save(update_fields=['is_published'])
        return redirect('catalog:product_detail', pk=product.pk)
