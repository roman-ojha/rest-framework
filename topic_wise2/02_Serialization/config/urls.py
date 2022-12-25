from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('detail/<int:pk>', views.student_detail, name='detail'),
    path('detail/', views.student_list, name='list'),
]
