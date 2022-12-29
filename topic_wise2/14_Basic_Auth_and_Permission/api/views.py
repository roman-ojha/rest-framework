from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

# For now we will ue BasicAuthentication, it is only for testing purpose not for production application

# Authentication Permission on 3 user:
# 1. Normal User: 'IsAuthenticated'
# 2. Admin(Staff): 'IsAdminUser'
# 3. Superuser


class StudentModelViewSet1(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # now we will add the authentication for for this particular View class
    authentication_classes = [BasicAuthentication]

    # Also we have to add the permission class so that we can specify who can access this View class
    # IsAuthenticated: can only access by the user who are authenticated user
    permission_classes = [IsAuthenticated]

    # If you don't want to specify these authentication class here
    # rather you want to apply these authentication & permission classes globally for all the routes in that case you have to add this on 'settings.py' file:
    """
        REST_FRAMEWORK = {
            'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.BasicAuthentication'],
            'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated']
        }
    """


class StudentModelViewSet2(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # Now because we had added the authentication class globally on 'settings.py' files
    # For every View class it will get apply but if you don't want to apply those globally added Authentication classes in This particular view in that case you can do this:
    # Now here you can change these authentication & permission classes as you want
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    # So here we override the globally applied authentication & permission classes
    # You can add multiple authentication & permission classes as you want

    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAdminUser,IsAuthenticated]
