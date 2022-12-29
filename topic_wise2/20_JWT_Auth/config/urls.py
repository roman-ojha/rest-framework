from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()

router.register('studentapi', views.StudentModelViewSet1, basename='student')

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include(router.urls)),
    # url to get token for given 'username' & 'password'
    # response Access Token & Refresh Token
    path('gettoken/', TokenObtainPairView.as_view(), name='gettoken'),
    # url to refresh token with given Refresh token
    # response new Access Token
    path('refreshtoken/', TokenRefreshView.as_view(), name='refreshtoken'),
    # url to verify the token, user provide the access Token
    path('verifytoken/', TokenVerifyView.as_view(), name='verifytoken'),
]
