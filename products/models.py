from django.db import models

# Create your models here.


class Product(models.Model):
    item_name = models.CharField(max_length=50,null=False, blank=False,unique=True)
    detail=models.CharField(max_length=200,null=True,blank=True)
    minimum_requirement=models.IntegerField()
    item_amount_available=models.IntegerField()
    row=models.IntegerField(null=True,blank=True)
    column=models.IntegerField(null=True,blank=True)
     
    def __str__(self): 
        return f"{self.item_name}"  
    
    verbose_name_plural = "اجناس"




class Vendors(models.Model):
    name = models.CharField(max_length=50,null=False, blank=False,unique=True)
    account=models.CharField(max_length=30,null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
     
    def __str__(self): 
        return f"{self.name}"  
    
    verbose_name_plural = "شرکت تولید کننده"