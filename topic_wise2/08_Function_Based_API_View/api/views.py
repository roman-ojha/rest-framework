from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
