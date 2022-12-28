from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

# If we are using 'ViewSet' class then we don't have to maintain the url
# we just how to create the router and then register that router then it will automatically handle all the CRUD operation with provided 'ViewSet' class

# Create Router object
router = DefaultRouter()

# Register Router with 'ViewSet' class
router.register('studentapi', views.StudentViewSet, basename='student')
# 'studentapi' is the base url for this router

urlpatterns = [
    # now we have to include that router that we create into django router
    # here we want to django router url to be '' it means that to access the 'studentapi' url we use 'studentapi/'
    path('', include(router.urls))
    # here we are including the urls of 'router' app the same way that we used to do before

    # Now to access the 'StudentViewSet' view class we have to use this url
    # http://127.0.0.1:8000/studentapi/
]
