from dataclasses import field
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # we want to access model 'get_discount' property as discount so because of that we will serialize that property into discount
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            # 'sale_price' is the reference to the Product property 'sale_price'
            'my_discount'
        ]

    def get_my_discount(self, obj):
        # now here to get access as 'my_discount' we have to return the property 'get_discount' of model
        # obj will contain the data and property of the model instance
        return obj.get_discount()
