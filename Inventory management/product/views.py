from rest_framework import viewsets
from .models import Category, Product,StockControl,Transaction, PurchaseOrder, SalesOrder
from .serializers import CategorySerializer, ProductSerializer, StockControlSerializer,TransactionSerializer,PurchaseSerializer,SalesSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer



class StockCotrolViewSet(viewsets.ModelViewSet):
    list_filter = ('Product',)
    queryset = StockControl.objects.all()
    serializer_class = StockControlSerializer


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset= PurchaseOrder.objects.all()
    serializer_class= PurchaseSerializer

class SalesViewSet(viewsets.ModelViewSet):
    queryset= SalesOrder.objects.all()
    serializer_class= SalesSerializer

# class ReportViewSet(viewsets.ModelViewSet):
#     queryset= Report.objects.all()
#     serializer_class= ReportSerializer

