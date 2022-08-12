from dataclasses import field
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)

    url_hyper = serializers.HyperlinkedIdentityField(
        view_name='product-detail', lookup_field='pk')
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Product
        fields = [
            'url',
            'edit_url',
            'url_hyper',
            'email',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]

    def create(self, validated_data):
        # email = validated_data.pop('email')
        obj = super().create(validated_data)
        # print(email, obj)
        return obj

    def update(self, instance, validated_data):
        email = validated_data.pop('email')
        instance.title = validated_data.get('title')

        return super().update(instance, validated_data)

    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
