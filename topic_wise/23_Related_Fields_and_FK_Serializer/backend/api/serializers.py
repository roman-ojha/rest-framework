from dataclasses import field
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


# now here we can create new serializer for User
# class UserPublicSerializer(serializers.Serializer):
class UserPublicSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)

    other_products = serializers.SerializerMethodField(read_only=True)

    # temp = serializers.CharField(read_only=True)
    # if this kind of temp doesn't exist in User model but you try to access it by 'serializers.Serializer' it will not throw an error but by 'serializers.ModelSerializer' and add Meta class it will throw an error

    class Meta:
        model = User
        fields = [
            'username',
            'id',
            'other_products'
            # 'temp'
        ]

    # and also we can get the product by defining it
    def get_other_products(self, obj):
        # request = self.context.get('request')

        # obj is user
        print(obj)
        user = obj
        # Now we can get the product using user
        my_products_qs = user.product_set.all()[:5]
        # now this data is get Serialize by 'UserProductInlineSerializer'
        return UserProductInlineSerializer(my_products_qs, many=True, context=self.context).data


class UserProductInlineSerializer(serializers.Serializer):
    url_hyper = serializers.HyperlinkedIdentityField(
        view_name='product-detail', lookup_field='pk', read_only=True)
    title = serializers.CharField(read_only=True)
