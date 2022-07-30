from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.ProductDetailAPIView.as_view())
    # pk (primary key) which is available by default inside model
    # because we have use class based view 'ProductDetailAPIView' we have to use it as view
]
