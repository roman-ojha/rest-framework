from rest_framework import generics, mixins
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
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)


product_create_view = ProductCreateAPIView.as_view()


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


product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
        return super().perform_update(serializer)


product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


product_destroy_view = ProductDestroyAPIView.as_view()


class ProductMixinView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    # the different between function based and class based view is that:
    # we don't condition for the different type of method rather we will write functions

    # ListModelMixin:
    #   -> Provides a .list(request, *args, **kwargs) method, that implements listing a queryset.
    #   -> If the queryset is populated, this returns a 200 OK response, with a serialized representation of the queryset as the body of the response. The response data may optionally be paginated.

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    # lookup_field is need for 'RetrieveModelMixin'

    def get(self, request, *args, **kwargs):
        # runs for get method

        print(args, kwargs)
        # for '<int:pk>/' endpoint & for 'RetrieveModelMixin'
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)

        # for 'list/' endpoint & 'ListModelMixin'
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # runs for post method
        # for '' endpoint & 'CreateModelMixin'
        # it return the create method
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # we also can add 'perform_create' function here because 'CreateModelMixin' provide this function
        # this function will get called when it have to create new model
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = 'hello this is the self written content'
        serializer.save(content=content)


product_mixin_view = ProductMixinView.as_view()


class CreateAPIView(mixins.CreateModelMixin, generics.GenericAPIView):
    # Actually all the class based APIView that we see before are inherited from Mixin & GenericAPIView EX for CreateAPIView
    pass


@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == "GET":
        pass
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)

        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"success": False, "msg": "invalid data"}, status=400)
