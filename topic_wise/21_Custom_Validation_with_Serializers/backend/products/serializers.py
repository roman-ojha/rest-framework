from dataclasses import field
from wsgiref.validate import validator
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validators import validate_title, validate_title_no_hello, unique_product_title


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)

    url_hyper = serializers.HyperlinkedIdentityField(
        view_name='product-detail', lookup_field='pk')
    email = serializers.EmailField(write_only=True)

    # another way to validate data field using serializers
    title = serializers.CharField(
        validators=[validate_title, validate_title_no_hello, unique_product_title])
    # we will add the list of validator that we can use for that field

    name = serializers.CharField(source='title', read_only=True)
    # we can even create new field inside serializer which will take the value of another field which we will define inside source argument

    class Meta:
        model = Product
        fields = [
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
            'my_discount'
        ]

    # to validated the specific data we will define function like this:
    # def validate_<field_name>()
    def validate_title(self, value):
        # in this case we are validating title
        # here we will get self & value the value is the title value
        # this function is now only for read only this can be able to use when we want to validate the data

        request = self.context.get('request')
        user = request.user

        # now by default we will return value like this
        # print(value)
        # return value

        qs = Product.objects.filter(user=user, title__exact=value)
        # so what we can do is and what we are doing here is we are checking does the 'value' exist in product data already

        qs = Product.objects.filter(title__iexact=value)
        # case insensitive

        if qs.exists():
            # after validate and if it fail the we can raise the error
            raise serializers.ValidationError(
                f"{value} is already a product name")
        # if title value doesn't exist as title in database then we will going to return exact value
        return value

    def create(self, validated_data):
        email = validated_data.pop('email')
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
