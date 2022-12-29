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
    => EX: or we can use '../client/app.py'

    => You can manage the response body as well as other thing for 'obtain_auth_token' api view by creating custom auth token
        -> we will create this inside './auth.py'
        -> and we will use that custom class on './urls.py'
4. Using Signals:
    -> We can generate a token for the user with user register, while creating the user
    -> for that we will create a signal that will get triggered when we are creating a new user
    -> signal is created inside './signals.py'
"""

"""
*) Token Authentication
    -> we will use '../client/app.py' to request to the api with Authentication header
"""


# Get generated token:
# Command: python manage.py drf_create_token <generated_user_token_username>


class StudentModelViewSet1(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Using TokenAuthentication
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
