from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('list/', views.StudentList.as_view()),
    path('create/', views.StudentCreate.as_view()),
    path('crud/', views.StudentAPI.as_view()),
    path('crud/<int:pk>', views.StudentAPI.as_view())
]
