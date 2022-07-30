from wsgiref import headers
from django.http import JsonResponse, HttpResponse
# JsonResponse: it accept a dictionary
# HttpResponse: it accept a string

import json

from django.forms.models import model_to_dict
# this is used in django form

from products.models import Product


def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
        # now we don't have to manually create dictionary the way that we did before
        # we can also declare the field that we want to add inside the dictionary
    return JsonResponse(data)
    # return HttpResponse(json.dumps(data), headers={"content-type": "application/json"})
    # because from HttpResponse we can only response string and we can't response dictionary after adding header as 'application/json'
    # we can convert dictionary into json string
    # But because we have to 'price' field which is in decimal and django can't Json Serialize Decimal value so rather on these case 'JsonResponse' handle dictionary pretty well
