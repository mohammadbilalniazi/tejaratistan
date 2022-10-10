from django.contrib import admin
# Register your models here.        
from purchase.models import Purchase_bill,Purchase_detail
@admin.register(Purchase_bill)
class Purchase_billAdmin(admin.ModelAdmin):
    #list_display=("item_name","item_amount","item_price","purchasing_date","return_qty")
    #list_display=get_model_fields(Purchase_bill)
    list_display=("payment","purchasing_date","purchaser","seller","discount","total_purchase_bill")
    
@admin.register(Purchase_detail)
class Purchase_detailAdmin(admin.ModelAdmin):
    list_display=("purchase_bill","product","item_amount","item_price","return_qty")
    
    # list_display=get_model_fields(Purchase_detail)
# @admin.register(Purchase)
# class Store_purchasedAdmin(admin.ModelAdmin):
#     list_display=("bill_no","payment","debit") 
