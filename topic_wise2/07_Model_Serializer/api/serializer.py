from rest_framework import serializers
from .models import Student

# Validators priority:
# 1. Validator function (run 1st)
# 2. Field level validation (run 2nd)
# 3. Object level validation (run 3rd)


# Validator function:
def start_with_r(value):
    # Define validator:
    if value[0].lower() != 'r':
        raise serializers.ValidationError("Name should be start with R")


# Model Serializer:
class StudentSerializer(serializers.ModelSerializer):
    # we can add validator to the 'name' field
    name = serializers.CharField(read_only=True, validators=[start_with_r])

    class Meta:
        # provide the model from which you want to create serializer
        model = Student

        # provide the field that you want on serializer
        fields = ['id', 'name', 'roll', 'city']

        # read_only validator for multiple field at once
        read_only_fields = ['name', 'roll']

        # adding extra property on serializer fields
        extra_kwargs = {
            'name': {'read_only': True, 'validators': [start_with_r]}}

    # 'create' & 'update' method is already been implemented

    # Field level validation
    def validate_roll(self, value):
        print(value)
        if value >= 200:
            raise serializers.ValidationError("Seat full")
        return value

    # Object level validation:
    # For multiple field
    def validate(self, attrs):
        name = attrs.get('name')
        city = attrs.get('city')
        if name.lower() == 'roman' and city.lower() != 'kathmandu':
            raise serializers.ValidationError(
                "City must be Kathmandu for Roman")
        return attrs
