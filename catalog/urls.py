from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ContactsView, ProductPublishView, ProductUnpublishView, CategoryProductsView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/publish/', ProductPublishView.as_view(), name='product_publish'),
    path('product/<int:pk>/unpublish/', ProductUnpublishView.as_view(), name='product_unpublish'),
    path('category/<int:pk>/products/', CategoryProductsView.as_view(), name='category_products'),
]
