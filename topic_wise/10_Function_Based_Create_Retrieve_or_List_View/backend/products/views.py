from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.http import Http404


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)


product_create_view = ProductCreateAPIView.as_view()


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_list_view = ProductListAPIView.as_view()


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)


product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


product_detail_view = ProductDetailAPIView.as_view()


@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    # pk(primary key) coming from route '<int:pk>/'
    method = request.method
    if method == "GET":
        pass
        # to get the single data from the data base we will use 'pk'

        # using Django Http404:
        """
        if pk is not None:
            # get request -> For Detail View
            queryset = Product.objects.filter(pk=pk)
            if not queryset.exists():
                # if given primary key doesn't exist then:
                raise Http404
                # this is get handled automatically by django
            return Response()
        """

        # Using Django rest framework 'get_object_or_404'
        if pk is not None:
            # get request -> For Detail View
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)

        # for List View:
        # first we will get the queryset
        queryset = Product.objects.all()
        # after that we will serialize that data
        data = ProductSerializer(queryset, many=True).data
        # after getting & serializing data we will response that data
        return Response(data)
    if method == "POST":
        # for Create View
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # logic/function 'perform_create' that we add on 'CreateAPIView' on the top
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"success": False, "msg": "invalid data"}, status=400)
