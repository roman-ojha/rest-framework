from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Product


def validate_title(value):
    qs = Product.objects.filter(title__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(
            f"{value} is already a product name")
    return value


def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError("Hello is now allowed")
    return value


unique_product_title = UniqueValidator(queryset=Product.objects.all())
# to check the uniqueness of any field rest_framework provide us the validator by default by passing queryset
