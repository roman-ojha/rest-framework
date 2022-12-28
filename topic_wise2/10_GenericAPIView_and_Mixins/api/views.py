from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# CRUD Operation Using GenericAPIView & Model Mixin:


# This view will Response list of record from database
# Implement GET Method
class StudentList(GenericAPIView, ListModelMixin):
    # For that we have to provide the queryset that it perform to response list of record
    queryset = Student.objects.all()

    # also we have to provide the serializer class for serializing the data
    serializer_class = StudentSerializer

    # ListModelMixin add implemented the list to get all the list of data so we will use that one
    def get(self, request, *args, **kwargs):
        # by returning list method now we can get all the list of data from 'Student' table
        return self.list(request, *args, **kwargs)


# This view will Create the 'Student' data and save into database
# Implement POST Method
class StudentCreate(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # CreateModelMixin implement the post method that will create a new object and save into database
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# This view will response the single object from the record
# Implement GET Method
# Required 'pk' from dynamic url
class StudentRetrieve(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # RetrieveModelMixin implement the get method that will response a single object from the record
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# This view will update the record in the database
# Implement PUT & PATCH Method
class StudentUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # UpdateModelMixin implement the put method that will update the record on database
    def put(self, request, *args, **kwargs):
        # this will work as Put as well as Patch
        return self.update(request, *args, **kwargs)


# This view will delete the record from the database
# Implement DELETE Method
class StudentDestroy(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # DestroyModelMixin implement the delete method that will delete the record from the database
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# CRUD Operation using all the Mixins
# On 'ListModelMixin' & 'CreateModelMixin' doesn't required 'pk'
# On 'RetrieveModelMixin', 'UpdateModelMixin' & 'DestroyModelMixin' does required 'pk'
# So these two are the Group so we will create different View class for this
class StudentLC(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# On 'RetrieveModelMixin', 'UpdateModelMixin' & 'DestroyModelMixin' does required 'pk'
class StudentRUD(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
