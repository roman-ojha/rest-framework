from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from .pagination import MyPageNumberPagination


# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # If you want to add PageNumberPagination globally in that case you have to add this inside 'settings.py' file
    # REST_FRAMEWORK = {
    #     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    #     'PAGE_SIZE': 5
    # }

    # If you want to add Pagination locally in that case you can add like this:
    # pagination_class = PageNumberPagination
    # But just by adding 'PageNumberPagination' on 'pagination_class' it won't work because we have not specify the 'page_size' so for that we can inherit the 'PageNumberPagination' and create a new class then we can add that class here

    # using the pagination that we created
    pagination_class = MyPageNumberPagination
