from django.core.cache import cache

from catalog.models import Product


CACHE_TIMEOUT = 60


def get_products_by_category(category_id):
    """Получает данные по товарам заданной категории из кеша, а если кеш пуст - генерирует из базы данных."""
    cache_key = f"category_{category_id}"
    products = cache.get(cache_key)

    if products is None:
        products = list(Product.objects.filter(category_id=category_id).select_related('category'))
        cache.set(cache_key, products, CACHE_TIMEOUT)

    return products