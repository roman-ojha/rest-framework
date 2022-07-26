from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):
    body = request.body
    print(body)
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    data['headers'] = request.headers
    data['content_type'] = request.content_type

    print(request.GET)
    data['params'] = dict(request.GET)
    print(data)
    return JsonResponse({"message": "Hello world"})
