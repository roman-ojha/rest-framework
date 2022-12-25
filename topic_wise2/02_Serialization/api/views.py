from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Model Object -> Single Student Data


def student_detail(request):
    # First getting Model object instance
    stu = Student.objects.get(id=1)
    # Serializing model object instance and converting into dict
    serialized = StudentSerializer(stu)
    print(serialized.data)
    # Converting serialized data into JSON
    json_data = JSONRenderer().render(data=serialized.data)
    print(json_data)

    # Returning json data as response to the client
    return HttpResponse(json_data, content_type='application/json')
