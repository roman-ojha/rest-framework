from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSet, ProductGenericViewSet

router = DefaultRouter()
router.register('products-abc', ProductViewSet, basename='abc')
# here we are assigning 'ProductViewSet' to the new router called 'products-abc'


router.register('products-xyz', ProductGenericViewSet, basename='xyz')

urlpatterns = router.urls
# now urlpatterns we ill gives us all the major or required url for all the method which
