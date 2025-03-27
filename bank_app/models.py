from django.db import models
from django.contrib.auth.models import AbstractUser # contains all logic for user model for django project
# Create your models here.

# when creating your own user model , you need to add AUTH_USER_MODEL="app_name.User"
class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=300,unique = True)
    number = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    # FileField can handle any extension
    image = models.ImageField(max_length=300)
    # abstractuser searches or creates user data using two fields(username and password), so using USERNAME_FIELD we are overriding username     
    #with email so that those two fields can be now (email and password)
    USERNAME_FIELD = 'email' 
    #Inside abstractuser there is a method to create superuser which requires username field so if username is overriden you need to specify it here as required field
    REQUIRED_FIELDS = ['username']
    
# RELATIONSHIP
    #OTM - one A table data can be value of many B table data, but one B table can only have one A table data as value
    #->one User can have Many accounts(use Foreign key)
    
    #OTO - one A table data can be value of one B table data only, also one B table data can only have one A table data
    #-> one user can have only one Account
    
    #MTM - one A table data can be value of many B table data, also B table data can have many A table data as value
    #-> one USer can have many Accounts, and one Account can have many USers
    
class Account(models.Model):
    account_name = models.CharField(max_length=200)
 
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null =True)#OTM, on_delete-> eg ram@gmail.com got deleted, aba Account ma tyo jata jata thyo tyo field ma NULL basne vo
    
    mobile_num = models.CharField(max_length =20)
    acc_num = models.CharField(max_length=200, unique=True)
    cheque_num = models.CharField(max_length=100,unique=True)
    
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True)
    
class Bank(models.Model):
    bank_name = models.CharField(max_length=200,unique=True)
    # If not unique-> error "name": "bank with this name already exists."
    short_name = models.CharField(max_length=50,unique=True)
    
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True)
    
class Statement(models.Model):
    #on_delete = models.CASCADE -> account delete vo vane tesko sab data udxa
    #on_Delete otm ma matra rakhne ho
    account = models.ForeignKey(Account, on_delete = models.SET_NULL, null=True)
    amount = models.FloatField()
    transaction_type = models.CharField(max_length =20)
    payment_type = models.CharField(max_length=20)
    description = models.TextField()
    withdrawn_by = models.CharField(max_length=200,null=True)
    bank = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True)
    cheque_num = models.CharField(max_length=200,null=True)
    deposited_by = models.CharField(max_length=200,null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True)
    
    
    
    
    
    