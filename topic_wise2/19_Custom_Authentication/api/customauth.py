from rest_framework.authentication import BaseAuthentication
from .models import Student
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

# Creating Custom Authentication


class CustomAuthentication(BaseAuthentication):
    # here we have to override the 'authenticate' method
    def authenticate(self, request):
        username = request.GET.get('username')
        if username is None:
            # return None means fail
            return None

        try:
            # if user name exist then we will check into the 'User' table
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # if user doesn't exist in that case we will raise the exception with 'AuthenticationFailed'
            raise AuthenticationFailed("No Such User")

        # if user exist in that case we will return the user
        return (user, None)
