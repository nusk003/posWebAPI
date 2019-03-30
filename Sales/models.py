from django.db import models
from Products.models import StockBranchSupplierItem
from Customer.models import Customer

# Create your models here.

class CustomerInvoice (models.Model):

    invoiceNo = models.CharField(max_length = 20)
    sellPrice = models.DecimalField(max_digits = 20,decimal_places = 2)
    costPrice = models.DecimalField(max_digits = 20 , decimal_places = 2)
    date = models.DateTimeField(auto_now = True)
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE)
    isCredit = models.BooleanField(default = False)
    deliveryType = models.IntegerField()
    isCancel = models.BooleanField(default = False)
    

class CustomerInvoiceItems (models.Model):

    invoice = models.ForeignKey(CustomerInvoice,on_delete = models.CASCADE,related_name = "Items",blank = True,null=True)
    product = models.ForeignKey(StockBranchSupplierItem,on_delete = models.CASCADE)
    costPrice = models.DecimalField(max_digits = 10,decimal_places = 2)
    sellPrice = models.DecimalField(max_digits = 10,decimal_places = 2)
    isCancel = models.BooleanField(default = False)

class CustomerAccounts (models.Model):

    customer = models.ForeignKey(Customer,on_delete = models.CASCADE)
    credit = models.DecimalField(max_digits = 20,decimal_places = 2,blank=True,null = True)
    debit = models.DecimalField(max_digits = 20,decimal_places = 2,blank=True,null=True)
    invoice = models.ForeignKey(CustomerInvoice,on_delete = models.CASCADE , blank = True,null=True)
    isDelete = models.BooleanField(default = False)
