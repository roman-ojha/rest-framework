from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from api.auth import CustomAuthToken

router = DefaultRouter()

router.register('studentapi', views.StudentModelViewSet1, basename='student')

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls'), name='rest_framework'),
    # To get or create token for user we have to use 'obtain_auth_token' view created by DRF
    # which accept 'username' & 'password' as credential
    path('gettoken/', obtain_auth_token),
    path('gettoken/', obtain_auth_token),

    # Using Custom class to generate token
    path('gettoken2/', CustomAuthToken.as_view())
]
