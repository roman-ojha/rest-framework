from rest_framework import serializers


# now here we can create new serializer for User
class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)

    # other_products = serializers.SerializerMethodField(read_only=True)

    # and also we can get the product by defining it
    # def get_other_products(self, obj):
    #     # obj is user
    #     print(obj)
    #     user = obj
    #     # Now we can get the product using user
    #     my_products
    #     return []
