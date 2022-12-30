from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('studentapi', views.StudentModelViewSet1, basename='student')

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('list/', views.StudentList.as_view()),
    path('create/', views.StudentCreate.as_view()),
    path('retrieve/<int:pk>/', views.StudentRetrieve.as_view()),
    path('update/<int:pk>/', views.StudentUpdate.as_view()),
    path('destroy/<int:pk>/', views.StudentDestroy.as_view()),
]
