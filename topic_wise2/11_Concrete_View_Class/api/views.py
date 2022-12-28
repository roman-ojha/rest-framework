from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView


# CRUD Operation Using Concrete View classes

# This view will Response list of record from database
# Implement GET Method
class StudentList(ListAPIView):
    # We have already learned about these property & method on GenericAPIView & Mixins tutorial
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# This view will Create the 'Student' data and save into database
# Implement POST Method
class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# This view will response the single object from the record
# Implement GET Method
# Required 'pk' from dynamic url
class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# This view will update the record in the database
# Implement PUT & PATCH Method
class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# This view will delete the record from the database
# Implement DELETE Method
class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# On 'ListCreateAPIView' doesn't required 'pk'
# Implement 'ListAPIView' & 'CreateAPIView'
class StudentLC(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# On 'RetrieveUpdateAPIView' does required 'pk'
# Implement 'RetrieveAPIView' & 'UpdateAPIView'
class StudentRU(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# On 'RetrieveDestroyAPIView' does required 'pk'
# Implement 'RetrieveAPIView' & 'DestroyAPIView'
class StudentRD(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# On 'RetrieveUpdateDestroyAPIView' does required 'pk'
# Implement 'RetrieveAPIView', 'UpdateAPIView' & 'DestroyAPIView'
class StudentRUD(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# NOTE: Your CRUD Operation can be perform by just two class 'ListCreateAPIView', 'RetrieveUpdateDestroyAPIView'
