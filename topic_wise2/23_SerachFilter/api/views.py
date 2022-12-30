from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import StudentSerializer
from .models import Student
from rest_framework.filters import SearchFilter


# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # adding SearchFilter class for filter_backends
    filter_backends = [SearchFilter]
    # we have to specify the field on the basis you want to search
    # search_fields = ['city']
    # EX: http://127.0.0.1:8000/list/?search=pokhara

    # search_fields = ['name','city']

    # start with:
    # search_fields = ['^name']

    # Exact match
    search_fields = ['=name']

    # by default DRF provide 'search' as query parameter and if you want to change it
    # in that case you want to add this inside 'settings.py' file
    # REST_FRAMEWORK = {
    #     'SEARCH_PARAM': 'q'
    # }
    # EX: http://127.0.0.1:8000/list/?q=Tony
