from django.urls import path
from . import views

urlpatterns = [
    # /api/products/1/
    path('<int:pk>/', views.product_alt_view),
    # /api/products/
    path('', views.product_alt_view),
    # /api/products/list
    path('list/', views.product_alt_view)
]
