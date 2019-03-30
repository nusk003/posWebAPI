from django.db import models
from Products.models import Item
 
# Create your models here.
class Package (models.Model) :

    packageName = models.CharField(max_length = 20)
    isDelete = models.BooleanField(default = False)
    isLive = models.BooleanField(default = True)
    price = models.DecimalField(max_digits = 20,decimal_places = 2)

class PackageItems (models.Model):

    package = models.ForeignKey(Package,on_delete = models.CASCADE)
    #item = models.ForeignKey(Item,on_delete = models.CASCADE)
    isDelete = models.BooleanField(default = False)

