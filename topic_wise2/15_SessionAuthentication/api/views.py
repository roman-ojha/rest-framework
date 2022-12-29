from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

# For now we will ue BasicAuthentication, it is only for testing purpose not for production application

# Permission Classes:
# 1. IsAuthenticatedOrReadOnly: can access all the method by authenticated user and can access GET, HEAD, OPTIONS method by unauthenticated user
# 2. DjangoModelPermissions: This is the Model Permission to add, update, read, delete on model from django
# 3. DjangoModelPermissionsOrAnonReadOnly: DjangoModelPermission + can Read by unauthenticated user


class StudentModelViewSet1(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Applied 'SessionAuthentication' Classes
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
