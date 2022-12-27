from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
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

    # Object level validation

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
