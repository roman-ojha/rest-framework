from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', views.StudentList.as_view()),
    path('listdf/', views.StudentListDF.as_view()),
    path('auth/', include('rest_framework.urls')),
]
