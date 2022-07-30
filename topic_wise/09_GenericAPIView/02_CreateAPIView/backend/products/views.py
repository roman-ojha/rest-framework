from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()

    # after we get queryset we have to serialize that data
    serializer_class = ProductSerializer
    lookup_field = 'pk'
