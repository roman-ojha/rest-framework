from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

# View that will create a new object and insert the data into database
# because we are using api version of Django where client could not have 'csrf_token' available in that case to ignore csrf error while insert data we have to put this specific decorator
@csrf_exempt
def student_create(request):
    # view
    if request.method == 'POST':
        # getting json data provided by the client
        json_data = request.body

        # now we have to convert this 'json_data' into stream
        stream = io.BytesIO(json_data)

        # now we have to convert this 'stream' data into python data: dict
        py_data = JSONParser().parse(stream=stream)

        # now we have to convert this python data into Complex data like 'Student' Model data
        serialized_data = StudentSerializer(data=py_data)

        # Now we will validate the Complex data
        if serialized_data.is_valid():
            # If valid this we will save/Insert that data into database
            serialized_data.save()

            # msg to respond to client
            res = {
                'msg': 'Data Inserted'
            }

            # we again have to convert this python data into JSON data
            json_response = JSONRenderer().render(res)

            # now we will response to the client
            return HttpResponse(json_response, content_type='application/json')
        else:
            # if some error occur while validating data then we will get that error on 'serialized_data.errors'
            json_response = JSONRenderer().render(serialized_data.errors)
            return HttpResponse(json_response, content_type='application/json')
