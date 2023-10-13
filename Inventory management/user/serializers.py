from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= User
        fields= '__all__'

class InventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= InventoryManager
        fields= '__all__'

class SaleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= SaleRepresentative
        fields= '__all__'

class PurchaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= PurchaseManager
        fields= '__all__'

class AdministratorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Administrator
        fields= '__all__'


