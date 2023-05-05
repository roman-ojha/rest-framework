from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.add_and_show, name="add_and_show"),
    path('delete/<int:id>/', views.delete_student, name="delete_student"),
    path('update/<int:id>/', views.update_student, name="update_student")
]
