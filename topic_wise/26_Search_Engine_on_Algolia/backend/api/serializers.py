from dataclasses import field
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserPublicSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'id',
        ]

    def get_other_products(self, obj):

        print(obj)
        user = obj
        my_products_qs = user.product_set.all()[:5]
        return UserProductInlineSerializer(my_products_qs, many=True, context=self.context).data


class UserProductInlineSerializer(serializers.Serializer):
    url_hyper = serializers.HyperlinkedIdentityField(
        view_name='product-detail', lookup_field='pk', read_only=True)
    title = serializers.CharField(read_only=True)
