from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):
    # To get the body from the request
    body = request.body  # return byte string of JSON data
    print(body)
    # by default body could be like this: b'{"query": "Hello world"}'
    # which will be in form of string

    # to convert this form of string into python dictionary
    data = {}
    try:
        # take string of JSON Data and convert it into Python Dict
        data = json.loads(body)
    except:
        pass
    print(data)
    # print(data.keys())
    # if we want to store request headers as data
    data['headers'] = request.headers
    data['content_type'] = request.content_type

    # get request parameter
    print(request.GET)  # get url query params
    data['params'] = dict(request.GET)
    print(data)
    return JsonResponse({"message": "Hello world"})
