from django.db import models


# Create your models here.
class Branch (models.Model):

    name = models.CharField(max_length = 20,unique =True)
    address = models.CharField(max_length = 100)
    phone = models.CharField (max_length = 12)
    isDelete = models.BooleanField(default = False)
    isLive = models.BooleanField(default = True)

