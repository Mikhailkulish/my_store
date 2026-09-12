from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, product_detail, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>/', product_detail, name='product_detail')
]
