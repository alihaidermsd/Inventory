from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet,StockCotrolViewSet,TransactionViewSet,PurchaseViewSet,SalesViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'transection', TransactionViewSet)
router.register(r'stock-control', StockCotrolViewSet)
router.register(r'purchase', PurchaseViewSet)
router.register(r'sale', SalesViewSet)


urlpatterns = [
    path('', include(router.urls)),
]



