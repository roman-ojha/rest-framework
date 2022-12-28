from rest_framework import serializers
from .models import Student


# Model Serializer:
class StudentSerializer(serializers.ModelSerializer):
    # we can add validator to the 'name' field
    name = serializers.CharField(read_only=True)

    class Meta:
        # provide the model from which you want to create serializer
        model = Student

        # provide the field that you want on serializer
        fields = ['id', 'name', 'roll', 'city']

        # read_only validator for multiple field at once
        read_only_fields = ['name', 'roll']

        # adding extra property on serializer fields
        extra_kwargs = {'name': {'read_only': True}}

    # 'create' & 'update' method is already been implemented

    # Field level validation
    # def validate_roll(self, value):
    #     print(value)
    #     if value >= 200:
    #         raise serializers.ValidationError("Seat full")
    #     return value
