from django.db import models
from Supplier.models import Supplier
from Branch.models import Branch

# Create your models here.
class Item (models.Model):

    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)
    isDelete = models.BooleanField(default = False)
    isLive = models.BooleanField(default = True)

class SupplierItem (models.Model) : 

    supplier = models.ForeignKey(Supplier,on_delete = models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    isDelete = models.BooleanField(default = False)
    isLive  = models.BooleanField(default = True)

class BranchSupplierItem (models.Model):

    supplierItem = models.ForeignKey(SupplierItem,on_delete = models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete = models.CASCADE)
    isDelete = models.BooleanField(default = False)
    isLive = models.BooleanField(default = True)

class StockBranchSupplierItem (models.Model):
    
    branchSupplierItem = models.ForeignKey(BranchSupplierItem,on_delete = models.CASCADE)
    stock = models.IntegerField()
    date = models.DateTimeField(auto_now = True)
    costPrice = models.DecimalField(max_digits = 20,decimal_places = 2)
    sellPrice = models.DecimalField(max_digits = 20,decimal_places = 2)   
    isDelete = models.BooleanField(default = False)
    isLive = models.BooleanField(default = True)

