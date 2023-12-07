from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Model Object -> Single Student Data


def student_detail(request, pk):
    # First getting Model object instance
    stu = Student.objects.get(id=pk)
    # Serializing model object instance and converting into dict
    serialized = StudentSerializer(stu)
    print(serialized.data)
    # Converting serialized data into JSON
    json_data = JSONRenderer().render(data=serialized.data)
    print(json_data)

    # Returning json data as response to the client
    return HttpResponse(json_data, content_type='application/json')

    # Return serialized data and convert into json and response json data
    # return JsonResponse(serialized.data)


def student_list(request):
    students = Student.objects.all()
    # If we are serializing model then we just have to pass the model instance
    # But if we are serializing the incoming data then we have to serialize like this: StudentSerializer(data=request.data)
    serialized = StudentSerializer(students, many=True)

    # if you don't want to render into json rather you want to render into json and then return using one method then you can use JsonResponse
    return JsonResponse(serialized.data, safe=False)
    # because here we are passing list of dict we have to use 'safe' False
