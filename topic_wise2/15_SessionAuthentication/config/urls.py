from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

# Create Router object
router = DefaultRouter()

# Register Router with 'ViewSet' class
router.register('studentapi', views.StudentModelViewSet1, basename='student')
router.register('studentapi2', views.StudentModelViewSet2, basename='student2')

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include(router.urls))
]
