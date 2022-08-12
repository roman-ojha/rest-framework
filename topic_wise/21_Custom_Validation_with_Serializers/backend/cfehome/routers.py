from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSet, ProductGenericViewSet

router = DefaultRouter()
router.register('products-abc', ProductViewSet, basename='abc')


router.register('products-xyz', ProductGenericViewSet, basename='xyz')

urlpatterns = router.urls
