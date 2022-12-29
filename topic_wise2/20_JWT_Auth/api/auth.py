from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


# Creating Custom AuthToken
class CustomAuthToken(ObtainAuthToken):
    # we need to override the post method because we get 'username' & 'password' as body
    def post(self, request, *args, **kwargs):
        # using the default serializer_class
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        # now we can get the authenticated user data
        user = serializer.validated_data['user']

        # getting or creating the token for the user
        token, created = Token.objects.get_or_create(user=user)

        # Now passing the custom response data into client
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
