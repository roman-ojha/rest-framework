from django.urls import path
from . import views

urlpatterns = [
    # /api/products/1/
    path('<int:pk>/', views.product_detail_view, name='product-detail'),
    # /api/products/
    path('', views.product_create_view),
    # /api/products/list
    path('list/', views.product_list_create_view, name='product-list'),
    # /api/products/1/update
    path('<int:pk>/update/', views.product_update_view, name='product-edit'),
    # /api/products/1/destroy
    path('<int:pk>/delete/', views.product_destroy_view),
]
