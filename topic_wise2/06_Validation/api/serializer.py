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


class StudentSerializer(serializers.Serializer):
    # implementing Validator function:
    name = serializers.CharField(max_length=100, validators=[start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    # Field level validation:
    # syntax: def validate_<fieldname>(self)
    def validate_roll(self, value):
        print(value)
        if value >= 200:
            # you can now raise the validation error like this
            raise serializers.ValidationError("Seat full")
            # Now when user try to insert the value with roll greater then 200 equal to then it will raise the error
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

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
