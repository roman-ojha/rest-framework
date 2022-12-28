from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('list/', views.StudentList.as_view()),
    path('create/', views.StudentCreate.as_view()),
    path('retrieve/<int:pk>/', views.StudentRetrieve.as_view()),
    path('update/<int:pk>/', views.StudentUpdate.as_view()),
    path('destroy/<int:pk>/', views.StudentDestroy.as_view()),
    path('lc/', views.StudentLC.as_view()),
    path('rud/<int:pk>/', views.StudentRUD.as_view()),
]
