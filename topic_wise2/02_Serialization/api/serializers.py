from rest_framework import serializers
from django.db import models


# Creating Student model Serializer that will convert complex model object into python dict
class StudentSerializer(serializers.Serializer):
    # we need to provide the field and it's type to get serialized
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
