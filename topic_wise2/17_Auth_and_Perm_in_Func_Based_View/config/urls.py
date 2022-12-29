from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student-api/', views.student_api, name='crud'),
    path('student-api/<int:pk>', views.student_api, name='crud-pk')
]
