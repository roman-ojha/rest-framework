from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from rest_framework.renderers import JSONRenderer
from .serializer import StudentSerializer
from django.http import HttpResponse


# Create your views here.

# we will create 1 function and perform all CRUD operation
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
