from django.urls import path
from . import views

urlpatterns = [
    # /api/products/1/
    path('<int:pk>/', views.product_detail_view),
    # /api/products/
    path('', views.product_create_view)
]