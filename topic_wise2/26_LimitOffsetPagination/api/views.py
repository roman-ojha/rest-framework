from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from .pagination import MyLimitOffsetPagination


# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # implemented 'LimitOffsetPagination'
    pagination_class = MyLimitOffsetPagination
