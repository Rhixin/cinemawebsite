from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


#Para ni help ig create user types, do u want to create admin acc ba or normal user ra ba
class AccountManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('Users must have a username')
        
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password=None):
        user = self.create_user(username, password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)  # Optional email field
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Permissions to access the admin site
    date_joined = models.DateTimeField(auto_now_add=True)  # Track when the user was created

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []  # Optional fields; you can add 'email' here if you want

    def __str__(self):
        return self.username


class Profile(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE) 
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.fname} {self.lname}'
    
    
    
    
        
        
        
    