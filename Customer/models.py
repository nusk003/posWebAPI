from django.db import models
#from Sales.models import CustomerInvoice
from Branch.models import Branch
# Create your models here.

class Customer (models.Model):

    name = models.CharField(max_length = 20)
    phone = models.CharField(max_length = 12)
    address = models.CharField(max_length = 100)
    branch = models.ForeignKey(Branch,on_delete = models.CASCADE,related_name = "Customers")
    isDelete = models.BooleanField(default = False)


