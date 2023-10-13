from django.contrib import admin
from .models import *
# Register your models here.

class UserMain(admin.ModelAdmin):
    list_display=('name','email')
    search_fields=('name',)
admin.site.register(User, UserMain)

class InventoryManagers(admin.ModelAdmin):
    list_display=('name','email')
    search_fields=('name',)
admin.site.register(InventoryManager, InventoryManagers)

class SaleRepresentatives(admin.ModelAdmin):
    list_display=('name','email')
    search_fields=('name',)
admin.site.register(SaleRepresentative, SaleRepresentatives)

class PurchaseManagers(admin.ModelAdmin):
    list_display=('name','email')
    search_fields=('name',)
admin.site.register(PurchaseManager, PurchaseManagers)

class Administrators(admin.ModelAdmin):
    list_display=('name','email')
    search_fields=('name',)
admin.site.register(Administrator, Administrators)

