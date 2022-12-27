from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from rest_framework.renderers import JSONRenderer
from .serializer import StudentSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View


@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            student = Student.objects.get(id=id)
            serialized_data = StudentSerializer(student)
            json_data = JSONRenderer().render(serialized_data.data)
            return HttpResponse(json_data, content_type="application/json")

        students = Student.objects.all()
        serialized_data = StudentSerializer(students, many=True)
        json_data = JSONRenderer().render(serialized_data.data)
        return HttpResponse(json_data, content_type="application/json")

    def post(self, request, *args, **kwargs):
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

        json_response = JSONRenderer().render(serialized_data.errors)
        return HttpResponse(json_response, content_type='application/json')

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        id = python_data.get('id', None)
        student = Student.objects.get(id=id)

        serializer = StudentSerializer(
            student, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {
                'msg': 'Data Updated'
            }
            json_response = JSONRenderer().render(res)
            return HttpResponse(json_response, content_type='application/json')

        json_response = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_response, content_type='application/json')

    def patch(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        id = python_data.get('id', None)
        student = Student.objects.get(id=id)

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

    def delete(self, request, *args, **kwargs):
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
        return JsonResponse(res, safe=False)
