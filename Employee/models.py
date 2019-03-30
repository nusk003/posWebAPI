from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,BaseUserManager
)

from rest_framework.authtoken.models import Token


from Branch.models import Branch

# Create your models here.
class UserManager (BaseUserManager) :

    def create_user (self,email,name,userType,password=None,is_staff=True,is_superuser=True):

        if not email:
            raise ValueError("User Must have an email address")

        if not password :
            raise ValueError("User must have a password")


        user_obj = self.model(
            email = self.normalize_email(email)
        )

        user_obj.set_password(password)
        user_obj.name = name
        user_obj.userType = userType
        user_obj.superuser = is_superuser
        user_obj.staff = is_staff
        user_obj.save(using=self.db)
        token = Token.objects.create(user=user_obj)

        return user_obj

    def create_staffuser (self,email,name,password=None):

        try:
            userType = UserType.objects.get(userType = "Super Admin")
        except:
            userType = UserType.objects.create(userType = "Super Admin")

        user = self.create_user(
            email,
            name,
            userType,
            password=password,
            is_staff = True,
            is_superuser = True
        )

        return user

    def create_superuser(self,email,name,password=None):

        try:
            userType = UserType.objects.get(userType = "Super Admin")
        except:
            userType = UserType.objects.create(userType = "Super Admin")

        user = self.create_user(
            email,
            name,
            userType,
            password=password,
           
            
        )
        return user

class UserType (models.Model):

    userType = models.CharField(max_length = 20)

class User (AbstractBaseUser):

    email = models.EmailField(unique = True)
    name = models.CharField(max_length = 20)
    address = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 12)
    active = models.BooleanField(default = True)
    userType = models.ForeignKey(UserType,on_delete=models.CASCADE)
    branch  = models.ForeignKey(Branch,on_delete = models.CASCADE,blank = True,null = True)
    staff = models.BooleanField(default=False)
    superuser = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__ (self):
        return self.email

    def get_full_name (self) :
        return self.email

    def get_short_name (self):
        return self.email

    def has_perm(self, perm, obj=None):
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_superuser(self):
        return self.superuser
    
 
