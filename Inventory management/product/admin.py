from django.contrib import admin
from .models import *
# Register your models here.

class Products(admin.ModelAdmin):
    list_display=('name','description','price','category','quantity')
    search_fields=('name',)
admin.site.register(Product, Products)

admin.site.register(Category)

class Transactions(admin.ModelAdmin):
    list_display=('product','quantity','transaction_type','timestamp')
    search_fields=('product',)
admin.site.register(Transaction, Transactions)

class StockControls(admin.ModelAdmin):
    list_display=('product','category')
    search_fields=('product',)
admin.site.register(StockControl, StockControls)

class PurchaseOrders(admin.ModelAdmin):
    list_display=('product','quantity')
    search_fields=('product',)
admin.site.register(PurchaseOrder, PurchaseOrders)

class SalesOrders(admin.ModelAdmin):
    list_display=('product','quantity')
    search_fields=('product',)
admin.site.register(SalesOrder, SalesOrders)


