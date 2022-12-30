from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttling import RomanRateThrottle
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.throttling import ScopedRateThrottle


class StudentModelViewSet1(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Adding Throttling on this view class
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # We can assign the rate globally for the throttle then we have to do it inside 'settings.py' file
    # But this way throttle rate will be same for all the view classes
    # If you want different throttle rate for different view classes in that case you have to inherit Throttle class and create new class
    # now we can add that class
    throttle_classes = [AnonRateThrottle, RomanRateThrottle]


# Creating different view class for different operation
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # We can throttle different part of api as well for that we have to use 'ScopedRateThrottle' class
    throttle_classes = [ScopedRateThrottle]
    # Now we have to define the throttle scope inside here
    throttle_scope = 'listview'
    # now we have to define the rate of this throttle scope inside 'settings.py' file


class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'createview'


class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'retrieveview'


class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'updateview'


class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'destroyview'
