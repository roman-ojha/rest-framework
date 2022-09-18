from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Product


@register(Product)
class ProductIndex(AlgoliaIndex):
    fields = [
        # so here we will define the field that we would authorized to get access by algolia
        'title',
        'content',
        'price',
        'user',
        'public',
    ]
