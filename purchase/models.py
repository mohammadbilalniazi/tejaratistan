from email.policy import default
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from products.models import Product,Vendors
from shopapp.models import Customer

class Purchase_bill(models.Model):
    payment=models.IntegerField()
    purchasing_date=models.DateField()
    purchaser=models.ForeignKey(User,on_delete=models.DO_NOTHING,max_length=30)
    seller=models.ForeignKey(Vendors,on_delete=models.DO_NOTHING)
    discount=models.IntegerField(default=0)  
    total_purchase_bill=models.IntegerField()
    
    verbose_name_plural = "Purchasing Bill"
    
    def __str__(self):
        return f"{self.id}"
 

 
class Purchase_detail(models.Model):
    purchase_bill=models.ForeignKey(Purchase_bill,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.DO_NOTHING,null=False, blank=False)
    item_amount = models.IntegerField()
    item_price=models.IntegerField()
    return_qty=models.IntegerField(null=True,blank=True)      
    def __str__(self):
        return f"{self.id}"
    
    verbose_name_plural = "Purchase detail"



