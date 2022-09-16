from urllib import request
from django.shortcuts import render
from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer

# now here we will implement views related to product search


class SearchListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # now we had implemented queryset and product related search on it's model
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        # we will get the query that user try to do
        user = None
        if self.request.user.is_authenticated:
            user = self.request.user
        results = qs.search(q, user=user)
        return results
