from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

# CRUD Operation Using GenericAPIView & Model Mixin:


# This view will Response list of record from database
# Implement GET Method
class StudentList(GenericAPIView, ListModelMixin):
    # For that we have to provide the queryset that it perform to response list of record
    queryset = Student.objects.all()

    # also we have to provide the serializer class for serializing the data
    serializer_class = StudentSerializer

    # ListModelMixin add implemented the list to get all the list of data so we will use that one
    def get(self, request, *args, **kwargs):
        # by returning list method now we can get all the list of data from 'Student' table
        return self.list(request, *args, **kwargs)


# This view will Create the 'Student' data and save into database
# Implement POST Method
class StudentCreate(GenericAPIView, CreateModelMixin):
    # For that we have to provide the queryset that it perform to response list of record
    queryset = Student.objects.all()

    # also we have to provide the serializer class for serializing the data
    serializer_class = StudentSerializer

    # CreateModelMixin implement the post method that will create a new object and save into database
    def post(self, request, *args, **kwargs):
        # by returning list method now we can get all the list of data from 'Student' table
        return self.create(request, *args, **kwargs)


# Class Based APIView
class StudentAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(
            student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(
            student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Updated"})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        id = pk
        Student.objects.get(id=id).delete()
        return Response({'msg': "Data deleted"})
