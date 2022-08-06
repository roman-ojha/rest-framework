from rest_framework.authentication import TokenAuthentication as BaseTokenAuth

# here we will override the default Authentication


class TokenAuthentication(BaseTokenAuth):
    keyword = "Bearer"
