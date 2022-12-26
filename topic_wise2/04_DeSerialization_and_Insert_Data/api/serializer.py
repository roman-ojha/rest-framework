from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    # To create the object and Insert into database we have to write this function
    def create(self, validate_data):
        return Student.objects.create(**validate_data)
