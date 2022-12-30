from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import StudentSerializer
from .models import Student
from rest_framework.filters import OrderingFilter


# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Adding Ordering Filter on filter_backends
    filter_backends = [OrderingFilter]
    # If you didn't add filed from which we want to order in that case we can order it will every filed

    # specifying the field from which we want to order
    ordering_fields = ['name']
