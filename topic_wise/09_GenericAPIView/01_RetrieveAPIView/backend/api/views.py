from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer
from django.http import JsonResponse


# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         data = ProductSerializer(instance).data
#     return Response(data, status=200)


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    # to get the data the is being send from client then we can get like this
    data = request.data

    serializer = ProductSerializer(data=request.data)
    # after we will post request by sending data from client side we can serialize that data that is being send from the client side and validate that data
    if serializer.is_valid(raise_exception=True):
        # if the post data is valid the we will get that data for farther work
        #  we can save that data
        instance = serializer.save()
        # here now 'instance' will contain the model instance
        print(instance)
        data = serializer.data
        # return JsonResponse(data)
        # if we will use Django 'JsonResponse' then it will through an error saying 'Forbidden (CSRF cookie not set.)' this is because the api views just for django the CSRF cookies need to be set this is the security feature of django
        # but incase of rest_framework we don't need that
        # so because of that we will going to use rest_framework
        return Response(data)
    return Response({"success": False, "msg": "invalid data"}, status=400)
