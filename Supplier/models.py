from django.db import models
#from Restock.models import SupplierInvoice 

# Create your models here.
class Supplier (models.Model):

    name  = models.CharField(max_length = 20)
    phone = models.CharField (max_length = 12)
    address = models.CharField(max_length = 100)
    isActive = models.BooleanField(default = True)




