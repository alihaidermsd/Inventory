from django.db import router
from django.urls import path,include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'inventorymanager', InventoryViewSet)
router.register(r'salerepresentative', SaleViewSet)
router.register(r'purchasemanager', PurchaseViewSet)
router.register(r'administrator', AdministratorViewSet)

urlpatterns = [
    path('',include(router.urls))
]