from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer
# to use ProductSerializer we have to first import it


@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(instance, fields=['id', 'title', 'price'])
        data = ProductSerializer(instance).data
        # now here rather we will use ProductSerializer instance to get the data of the model and using it we will be able to access the property of that model as well
    return Response(data, status=200)
