from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializsers import StudentSerializer
from .models import Student


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
