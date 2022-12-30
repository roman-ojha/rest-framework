from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializsers import StudentSerializer
from .models import Student
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class StudentList(ListAPIView):
    # queryset = Student.objects.all()

    # if you want to filter by 'passby' field get the Student 'passby' xxx in that case we can change the query set like this:
    # queryset = Student.objects.filter(passby='roman')
    # But we will set the query set as 'all()'
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # and we will filter the queryset with those user that get logged in
    # so if 'roman' user is authenticated and try to call this api in that case we want to filter the student 'passby' 'roman' user
    # for that we have to override the 'get_queryset' method
    def get_queryset(self):
        user = self.request.user
        print(user)
        return Student.objects.filter(passby=user)


class StudentListDF(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    """
        -> But to filter base of field we will use 'django-filter' package:
        -> pip install django-filter
        -> add app on INSTALLED_APPS on 'settings.py' file
        -> we can globally enable django_filter on 'settings.py' file
                REST_FRAMEWORK = {
                    'DEFAULT_FILTER_BACKENDS': ['django_filter.rest_framework.DjangoFilterBackend']
                }
            
    """
    # now here we will specify the fields from which we want to filter
    # filterset_fields = ['city']
    # EX: http://127.0.0.1:8000/listdf/?city=pokhara

    # But if you don't want to use 'django-filter' globally in that case you can specify the filter_backends for every view class
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city', 'passby']
