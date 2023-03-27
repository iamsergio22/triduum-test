from rest_framework import routers
from .api import ProductViewSet,OrderViewSet,OrderDetailViewSet


router = routers.DefaultRouter()
#products
router.register(r'products', ProductViewSet)
#orders
router.register(r'orders', OrderViewSet)
#orders-detail
router.register(r'order-detail', OrderDetailViewSet)

urlpatterns = router.urls

