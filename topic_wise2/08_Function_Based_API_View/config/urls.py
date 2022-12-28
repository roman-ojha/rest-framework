from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hw/', views.hello_world, name='hw'),
    path('hwp/', views.h_w, name='hwp'),
    path('hwgp/', views.h_w_gp, name='hwgp'),
    path('crud/', views.student_api, name='crud'),
    path('crud/<int:pk>', views.student_api_2, name='crud-pk')
]
