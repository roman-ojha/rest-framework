from dataclasses import field
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    # create new url serializers
    # for 'product-detail'
    url = serializers.SerializerMethodField(read_only=True)
    # for 'product-edit'
    edit_url = serializers.SerializerMethodField(read_only=True)

    # another method
    url_hyper = serializers.HyperlinkedIdentityField(
        view_name='product-detail', lookup_field='pk')
    # 'HyperlinkedIdentityField' only work for 'ModelSerializer'

    class Meta:
        model = Product
        fields = [
            'url',
            # add it into field
            'edit_url',
            'url_hyper',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]

    def get_url(self, obj):
        # serializer method
        # return f"/api/products/{obj.pk}/"
        # now this will return the url or that particular obj/product

        # but if we will change the path to another else then we have to manually change it here as well to solve that problem we will going to use 'reverse'
        request = self.context.get('request')
        # first we will get the request object
        # we will by default get the request object if we are now manually declare/define serializer inside views
        if request is None:
            return None
        # if request exist then we will going to put it as an argument inside reverse
        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)
        # 'product-detail' is coming from the name of the urls that we define inside 'products/urls.py'
        # now this will return the whole path like: 'http://127.0.0.1:8000/api/products/1/' from this get_url function

    def get_edit_url(self, obj):
        # this urls is for '<int:pk>/update/'
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)
        # this will return ex: 'http://127.0.0.1:8000/api/products/1/update/'
        # NOTE: if you don't want these url for some of the view then you have to create different Serializers Class for that specific View

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
