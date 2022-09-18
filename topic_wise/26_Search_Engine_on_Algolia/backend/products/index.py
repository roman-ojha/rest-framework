from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Product


@register(Product)
class ProductIndex(AlgoliaIndex):
    should_index = 'is_public'
    # now here we are indexing only the public data not the private
    # and 'is_public' is the function that we write down into Product model which will return true or false

    fields = [
        # so here we will define the field that we would authorized to get access by algolia
        'title',
        'content',
        'price',
        'user',
        'public',
    ]

    # we will also add tags for searching
    tags = 'get_tags_list'
    # 'get_tags_list' is the function that we define inside products models
