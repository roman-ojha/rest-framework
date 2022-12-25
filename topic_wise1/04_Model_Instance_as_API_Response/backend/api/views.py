from django.http import JsonResponse
import json
from products.models import Product


def api_home(request, *args, **kwargs):
    # now here we will get the render data from the database
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # if model_data exist
        # add data to dict
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
    #  return JSON to client
    return JsonResponse(data)
