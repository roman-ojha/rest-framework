from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

"""
Generate token through:
1. http://127.0.0.1:8000/adminauthtoken/tokenproxy/add/
2. Command: python manage.py drf_create_token <username>
3. Using API endpoints: create endpoint inside ./urls.py using 'obtain_auth_token' function based view
    => EX: we can use command line to access the api endpoint
        -> install 'httpie' package
        -> pip install httpie
        -> Command: http POST http://127.0.0.1:8000/gettoken/ username="" password= "password"
        -> Response(default): {'token': 'd8b1ad0a0a28d062b9e9ad2e6c76a0cd00155ade'}

    => You can manage the response body as well as other thing for 'obtain_auth_token' api view by creating custom auth token
        -> we will create this inside './auth.py'
        -> and we will use that custom class on './urls.py'
"""


# Get generated token:
# Command: python manage.py drf_create_token <generated_user_token_username>


class StudentModelViewSet1(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # authentication_classes = [SessionAuthentication]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
