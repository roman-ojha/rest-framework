from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # As we can see that both the 'ProductCreateAPIView' & 'ProductDetailAPIView' looks same but there generic is different means that one use 'RetrieveAPIView' to get the mentioned queryset and one is used to create data and save it into database

    # while create using this view we want to assign something then
    def perform_create(self, serializer):
        # this method can be called inside CreateAPIView

        # to get the data that is been validated
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            # if client did not send by client then we will save content value as title
            content = title
        serializer.save(content=content)


product_create_view = ProductCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


product_detail_view = ProductDetailAPIView.as_view()
