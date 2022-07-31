from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # As we can see that both the 'ProductCreateAPIView' & 'ProductDetailAPIView' looks same but there generic is different means that one use 'RetrieveAPIView' to get the mentioned queryset and one is used to create data and save it into database


product_create_view = ProductCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


product_detail_view = ProductDetailAPIView.as_view()
