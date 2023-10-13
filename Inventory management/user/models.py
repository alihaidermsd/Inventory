from django.db import models
from django.shortcuts import HttpResponse
# Create your models here.

class User(models.Model):
    name= models.CharField(max_length=80)
    email= models.EmailField(max_length=50)
    address= models.CharField(max_length=250)
    phone= models.IntegerField()

class InventoryManager(models.Model):
    name= models.CharField(max_length=80)
    email= models.EmailField(max_length=250)
    passsword= models.CharField(max_length=100)
    r_passsword= models.CharField(max_length=100)
    if passsword==r_passsword:
        pass
    else:
        HttpResponse("Password not matched")


class SaleRepresentative(models.Model):
    name= models.CharField(max_length=80)
    email= models.EmailField(max_length=250)
    passsword= models.CharField(max_length=100)
    r_passsword= models.CharField(max_length=100)
    if passsword==r_passsword:
        pass
    else:
        HttpResponse("Password not matched")

class PurchaseManager(models.Model):
    name= models.CharField(max_length=80)
    email= models.EmailField(max_length=250)
    passsword= models.CharField(max_length=100)
    r_passsword= models.CharField(max_length=100)
    if passsword==r_passsword:
        pass
    else:
        HttpResponse("Password not matched")


class Administrator(models.Model):
    name= models.CharField(max_length=80)
    email= models.EmailField(max_length=250)
    passsword= models.CharField(max_length=100)
    r_passsword= models.CharField(max_length=100)
    if passsword==r_passsword:
        pass
    else:
        HttpResponse("Password not matched")