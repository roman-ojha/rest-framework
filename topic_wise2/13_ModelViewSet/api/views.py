from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets


# CRUD Operation using 'ModelViewSet'
class StudentModelViewSet(viewsets.ModelViewSet):
    # We just have to provide these property and all the CRUD operation will handle by this view class
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# This view only support Ready only Methods
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
