from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    # this function will use to update the data into database
    def update(self, instance, validated_data):

        # instance: old data
        # validate_data: new data
        # so now here we will going to get the validated_data if exit
        # if validate_data didn't exist then we will assign the old data into instance
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
