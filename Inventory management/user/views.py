from django.shortcuts import render,redirect,HttpResponse
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class= UserSerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset= InventoryManager.objects.all()
    serializer_class= InventorySerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset= SaleRepresentative.objects.all()
    serializer_class= SaleSerializer

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset= PurchaseManager.objects.all()
    serializer_class= PurchaseSerializer

class AdministratorViewSet(viewsets.ModelViewSet):
    queryset= Administrator.objects.all()
    serializer_class= AdministratorSerializer


