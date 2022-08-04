from django.urls import path
from . import views

urlpatterns = [
    # /api/products/1/
    path('<int:pk>/', views.product_mixin_view),
    # /api/products/
    path('', views.product_mixin_view),
    # /api/products/list
    path('list/', views.product_mixin_view),
    # /api/products/1/update
    path('<int:pk>/update/', views.product_update_view),
    # /api/products/1/destroy
    path('<int:pk>/delete/', views.product_destroy_view),
]
