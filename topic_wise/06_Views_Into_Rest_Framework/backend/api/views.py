from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.response import Response
# here we will use 'Response' for response rather the 'JsonResponse'
from rest_framework.decorators import api_view
# another thing that we will need is a 'api_view' decorator


@api_view(["GET", "POST"])
# now here we can declare what method that we want it to allow by default from any given api request
def api_home(request, *args, **kwargs):
    # Now this is a django rest framework(DRF) API view
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    return Response(data, status=200)
