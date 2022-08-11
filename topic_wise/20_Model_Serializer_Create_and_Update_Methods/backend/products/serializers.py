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
    # so what if every time you create a new product you want to have a one of email send to somebody
    email = serializers.EmailField(write_only=True)
    # we will use 'write_only' because it doesn't exist inside model and we can write on that field

    class Meta:
        model = Product
        # that the 'ProductSerializer' will do is it will create the data inside the 'Product' model itself
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
        # which creating new model data we can override that method
        # so when it will create the new data it will also validate that data
        # and so this create method will take that validated data
        # by default : Product.objects.create(**validated_data)

        # email = validated_data.pop('email')
        # now here because email doesn't exist inside model field we have to pop it of so that which create new model from the validated_date it wouldn't through error
        # after popping it up we will now get the email value from the serializer
        obj = super().create(validated_data)
        # print(email, obj)

        # default return value
        return obj

    # if there is not an instance then it will call 'create' method but if there is an instance then it will call 'update' method
    def update(self, instance, validated_data):
        # this method will update the instance it self
        email = validated_data.pop('email')
        instance.title = validated_data.get('title')

        # update instance data
        # return instance
        # or
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
