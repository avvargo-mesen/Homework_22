from .models import Product
from django.core.cache import cache

def get_products_by_category(category_id):
    products = cache.get(f'category_{category_id}')
    if not products:
        products = Product.objects.filter(category_id=category_id)
        cache.set(f'category_{category_id}', products, 60 * 50)


    return products

