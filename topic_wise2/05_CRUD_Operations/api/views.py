from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from rest_framework.renderers import JSONRenderer
from .serializer import StudentSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


# NOTE: all the process that we are doing here had been done in previous tutorial

# we will create 1 function and perform all CRUD operation
@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        # Reading Operation:
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        # getting id if exist
        id = python_data.get('id', None)
        if id is not None:
            # If id exist then we will return single Student detail
            student = Student.objects.get(id=id)
            serialized_data = StudentSerializer(student)
            json_data = JSONRenderer().render(serialized_data.data)
            return HttpResponse(json_data, content_type="application/json")

        # If id doesn't exist in that case we have to response all the Student Data
        students = Student.objects.all()
        serialized_data = StudentSerializer(students, many=True)
        json_data = JSONRenderer().render(serialized_data.data)
        return HttpResponse(json_data, content_type="application/json")

    elif request.method == "POST":
        # Insert Operation
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serialized_data = StudentSerializer(data=python_data)
        if serialized_data.is_valid():
            serialized_data.save()
            res = {
                'msg': 'Data Inserted'
            }
            json_response = JSONRenderer().render(res)
            return HttpResponse(json_response, content_type='application/json')

        # If not valid
        json_response = JSONRenderer().render(serialized_data.errors)
        return HttpResponse(json_response, content_type='application/json')

    elif request.method == "PUT":
        # Partial Update Operation
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        # first we will get the id to update that record
        id = python_data.get('id', None)
        student = Student.objects.get(id=id)

        # Partial update:
        serializer = StudentSerializer(
            student, data=python_data, partial=True)
        # StudentSerializer(<instance>,<new_data>)
        if serializer.is_valid():
            serializer.save()
            res = {
                'msg': 'Data Updated'
            }
            json_response = JSONRenderer().render(res)
            return HttpResponse(json_response, content_type='application/json')

        # If not valid
        json_response = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_response, content_type='application/json')

    elif request.method == "PATCH":
        # Complete Update Operation
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        id = python_data.get('id', None)
        student = Student.objects.get(id=id)

        # Complete update:
        serializer = StudentSerializer(
            student, data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {
                'msg': 'Data Updated'
            }
            json_response = JSONRenderer().render(res)
            return HttpResponse(json_response, content_type='application/json')

        json_response = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_response, content_type='application/json')

    elif request.method == "DELETE":
        # Delete operation
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        student = Student.objects.get(id=id)
        student.delete()
        res = {
            'msg': 'Data Deleted'
        }
        # json_response = JSONRenderer().render(res)
        # return HttpResponse(json_response, content_type='application/json')

        # Other way to response the Json data
        return JsonResponse(res, safe=False)
