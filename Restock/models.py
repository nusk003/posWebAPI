from django.db import models
from Supplier.models import Supplier
from Products.models import Item
from Branch.models import Branch

# Create your models here.

class SupplierInvoice (models.Model):

    supplier = models.ForeignKey(Supplier,on_delete = models.CASCADE,related_name = "Invoices")
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,related_name = "Invoices")
    date = models.DateTimeField(auto_now = True)
    isCredit = models.BooleanField(default = False)
    isCancel = models.BooleanField(default = False)
    costPrice = models.DecimalField(max_digits = 20 , decimal_places = 2)
    sellPrice = models.DecimalField(max_digits = 20 , decimal_places = 2)


class SupplierInvoiceItem (models.Model):

    invoice = models.ForeignKey(SupplierInvoice,on_delete = models.CASCADE,related_name = "Items")
    item = models.ForeignKey(Item,on_delete = models.CASCADE)
    costPrice = models.DecimalField(max_digits = 20 , decimal_places = 2)
    sellPrice = models.DecimalField(max_digits = 20 , decimal_places = 2)
    isCancel = models.BooleanField(default = False)


class SupplierAccount (models.Model) :

    invoice = models.ForeignKey(SupplierInvoice,on_delete=models.CASCADE,blank = True,null = True)
    supplier = models.ForeignKey(Supplier,on_delete = models.CASCADE,related_name = "Accounts")
    credit = models.DecimalField (max_digits = 20,decimal_places = 2,blank = True,null = True)
    debit = models.DecimalField (max_digits = 20,decimal_places = 2,blank = True,null = True)
    isDelete = models.BooleanField(default = False)