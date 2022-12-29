from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from rest_framework import status


@api_view(['GET'])
def hello_world(request):
    return Response({'msg': 'Hello world'})


@api_view(['POST'])
def h_w(request):
    if request.method == "POST":
        data = request.data
        print(data)
        return Response({'msg': 'This is post request'})


@api_view(['GET', 'POST'])
def h_w_gp(request):
    if request.method == "GET":
        return Response({'msg': 'This is get request'})
    elif request.method == "POST":
        data = request.data
        return Response({'msg': 'This is post request', 'data': data})


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request):
    if request.method == 'GET':
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


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api_2(request, pk=None):
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
