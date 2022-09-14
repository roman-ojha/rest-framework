from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/products/', include('products.urls')),
    path('api/v2/', include('cfehome.routers'))
    # adding router if we will go to this router we will see list of all register router
]
