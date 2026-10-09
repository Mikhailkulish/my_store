from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED

def get_products_by_category(category_id):
    """Получает данные по товарам заданной категории из кеша, а если кеш пуст - генерирует из базы данных."""
    if not CACHE_ENABLED:
        return Product.objects.filter(category_id=category_id).select_related('category')
    key = f'products_by_category_{category_id}'
    products = cache.get(key)
    if products is None:
        products = list(Product.objects.filter(category_id=category_id).select_related('category'))
        cache.set(key, products, 60)
    return products