#This model file contains our custom user & superuse model

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

'''
    Basically a manager is used to provide an interface through which
    DB queries are provided to the Django Models
    For our Custom User Model, we are going to modify the inital QuerySet & provide
    2 additional methods to create a normal user and a superuser
'''

class UserManager(BaseUserManager):
    
    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        user = self.model(email=self.normalize_email(email), **extra_fields)    #normalize_email lower cases the domain part
        user.set_password(password) 
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)

'''
    This is our custom user with
'''
class UserData(AbstractUser):

    username = None
    name = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name