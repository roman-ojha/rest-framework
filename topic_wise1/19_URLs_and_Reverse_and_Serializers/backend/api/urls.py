from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('auth/', obtain_auth_token),
    # 'obtain_auth_token' will generate token based after use get login using 'username' and password
    path('', views.api_home, name="home")
]
