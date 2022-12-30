from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializsers import StudentSerializer
from .models import Student


# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
