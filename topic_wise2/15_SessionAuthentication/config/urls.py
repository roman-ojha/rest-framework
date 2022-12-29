from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('studentapi', views.StudentModelViewSet1, basename='student')

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include(router.urls)),
    # To authenticated to user for 'SessionAuthentication' DRF provide the url where we can go and authenticated ourself
    path('auth/', include('rest_framework.urls'), name='rest_framework')
    # after adding this we can see the 'Login' button on DRF Browsable API
]
