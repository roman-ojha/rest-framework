from dataclasses import field
from wsgiref.validate import validator
from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from .validators import validate_title, validate_title_no_hello, unique_product_title
from api.serializers import UserPublicSerializer


class ProductInlineSerializer(serializers.Serializer):
    url_hyper = serializers.HyperlinkedIdentityField(
        view_name='product-detail', lookup_field='pk', read_only=True)
    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url_hyper = serializers.HyperlinkedIdentityField(
        view_name='product-detail', lookup_field='pk')
    email = serializers.EmailField(write_only=True)
    title = serializers.CharField(
        validators=[validate_title, validate_title_no_hello, unique_product_title])
    name = serializers.CharField(source='title', read_only=True)

    class Meta:
        model = Product
        fields = [
            'owner',
            'url',
            'edit_url',
            'url_hyper',
            'email',
            'pk',
            'title',
            'name',
            'content',
            'price',
            'sale_price',
            'public',
        ]

    def get_my_user_data(self, obj):
        return{
            "username": obj.user.username
        }

    def validate_title(self, value):
        request = self.context.get('request')
        user = request.user
        qs = Product.objects.filter(user=user, title__exact=value)
        qs = Product.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(
                f"{value} is already a product name")
        return value

    def create(self, validated_data):
        email = validated_data.pop('email')
        obj = super().create(validated_data)
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
