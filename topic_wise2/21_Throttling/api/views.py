from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttling import RomanRateThrottle


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
