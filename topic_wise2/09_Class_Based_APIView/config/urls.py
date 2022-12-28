from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('crud/', views.StudentAPI.as_view(), name='crud'),
    path('crud/<int:pk>', views.StudentAPI.as_view(), name='crud-pk')
]
