from dataclasses import field
from wsgiref.validate import validator
from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from .validators import validate_title, validate_title_no_hello, unique_product_title
from api.serializers import UserPublicSerializer
# now we will import that UserPublicSerializer Here


# we will also add new ProductInlineSerializer here
class ProductInlineSerializer(serializers.Serializer):
    url_hyper = serializers.HyperlinkedIdentityField(
        view_name='product-detail', lookup_field='pk', read_only=True)
    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    # now here we will add field for serializer user data
    my_user_data = serializers.SerializerMethodField(read_only=True)

    # Now after creating new UserPublicSerializer we can add that here
    user = UserPublicSerializer(read_only=True)
    owner = UserPublicSerializer(source='user', read_only=True)
    # also we can be able to use owner with source as user

    related_products = ProductInlineSerializer(
        source='user.product_set.all', read_only=True, many=True)
    # and access that ProductInlineSerializer here

    my_discount = serializers.SerializerMethodField(read_only=True)
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
            'user',
            'owner',
            # now that User data can add
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
            'my_discount',
            'my_user_data',
            # add that field here
            'related_products'
            # and add that related_products here
        ]

    # now we can define that my_user_data
    def get_my_user_data(self, obj):
        return{
            "username": obj.user.username
        }
        # But this is not the prefer way to serialize the related field data

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

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
