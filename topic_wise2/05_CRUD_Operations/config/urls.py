from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crud/', views.student_api, name='crud'),
    path('class-crud/', views.StudentAPI.as_view(), name='class-crud'),
]
