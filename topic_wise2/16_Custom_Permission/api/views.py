from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from .custompermissions import MyPermission


class StudentModelViewSet1(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    authentication_classes = [SessionAuthentication]

    # Adding Custom permission classes
    permission_classes = [MyPermission]
