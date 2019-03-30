from django.db import models
from Sales.models import CustomerInvoice
from Employee.models import User

# Create your models here.
class VehicleType (models.Model):

    vehicleType = models.CharField(max_length = 20)


class Vehicle (models.Model):

    vehicleNo = models.CharField(max_length = 20)
    vehicleType = models.ForeignKey(VehicleType,on_delete = models.CASCADE)
    isDelete = models.BooleanField(default = False)

class DeliveryCharge(models.Model):

    maxDistance = models.IntegerField()
    minDistance = models.IntegerField()
    charge = models.DecimalField(max_digits = 6,decimal_places = 2)
    vehicleType = models.ForeignKey(VehicleType,on_delete = models.CASCADE)

class Delivery (models.Model):

    invoice = models.ForeignKey(CustomerInvoice,on_delete = models.CASCADE,related_name = "Delivery")
    distance = models.DecimalField(max_digits=10,decimal_places=2)
    deliveryCharge = models.DecimalField(max_digits = 10,decimal_places = 2)
    driver = models.ForeignKey(User,on_delete = models.CASCADE,blank = True,null = True,related_name="Delivery")
    vehicle = models.ForeignKey(Vehicle,on_delete = models.CASCADE,blank = True,null = True,related_name="Delivery")
    status = models.IntegerField()
    isCancel = models.BooleanField(default = False)