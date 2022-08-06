from rest_framework.authentication import TokenAuthentication as BaseTokenAuth
from rest_framework.authtoken.models import Token


class TokenAuthentication(BaseTokenAuth):
    # here we will override the default Authentication

    # custom Authentication header keyword
    keyword = "Bearer"
