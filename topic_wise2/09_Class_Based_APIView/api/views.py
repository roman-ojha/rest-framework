from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from rest_framework import status

# NOTE: if you use 'api_view' decorators in that case you will get Browsable API on you Browser

# using DRF 'api_view' to create view
# @api_view()  # default GET request is accepted


@api_view(['GET'])  # Or you can provide the GET method both are same
def hello_world(request):
    return Response({'msg': 'Hello world'})


# POST Method view
@api_view(['POST'])
def h_w(request):
    if request.method == "POST":
        # get data passed by requested user
        data = request.data
        print(data)
        return Response({'msg': 'This is post request'})


# GET & POST Method view
@api_view(['GET', 'POST'])
def h_w_gp(request):
    if request.method == "GET":
        return Response({'msg': 'This is get request'})
    elif request.method == "POST":
        # get data passed by requested user
        data = request.data
        return Response({'msg': 'This is post request', 'data': data})


# CRUD Operation Example with Function based view
# NOTE: CRUD Operation example had been done on previous tutorial without using 'api_view' so please refer that one as well
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request):
    if request.method == 'GET':
        # Now we can get json object on python like this rather then what we did before on previous CRUD Operation example
        id = request.data.get('id')
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PUT":
        id = request.data.get('id')
        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(
            student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        id = request.data.get('id')
        student = Student.objects.get(id=id).delete()
        return Response({'msg': "Data deleted"})


# Now after implementing this view api function we can access the 'pk' value from url on Browsable API URL as well
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api_2(request, pk=None):
    # here we will get id from dynamic url rather then from 'request.data'
    if request.method == 'GET':
        id = pk
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PUT":
        id = pk
        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(
            student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PATCH":
        id = pk
        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(
            student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Updated"})
        return Response(serializer.errors)
    elif request.method == "DELETE":
        id = pk
        student = Student.objects.get(id=id).delete()
        return Response({'msg': "Data deleted"})
