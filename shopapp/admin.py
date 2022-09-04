from django.contrib import admin
#from shopapp.models import Log,Customer,Customer_kahatha_received,Product,Purchase_detail,Purchase_bill,Roznamcha,Initial_asset,Sale_bill,Sales_detail
from products.models import Vendors,Product
from shopapp.models import Customer, Supplier , Supplier_Ledger , Customer_Ledger , Log ,Purchase_bill, Purchase_detail,Sale_bill,Sales_detail,Roznamcha,Asset
from django.utils.html import format_html
# Register your models here.

 
 
admin.site.site_header=format_html("<h1 style='color:red; font-weight:bold; text-align:center; font-size:40px'>تجارتستان</h1>")

def get_model_fields(model):
    field_list=[field.name for field in model._meta.get_fields()]
    return field_list

  
@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display=get_model_fields(Log)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    
    list_display=("name","tazkira","contact")
    

@admin.register(Customer_Ledger)
class Customer_LedgerAdmin(admin.ModelAdmin):
    list_display=get_model_fields(Customer_Ledger)
    #list_display=("customer","receiver","narration","amount_paid","payment_date")
    
@admin.register(Roznamcha)
class RoznamchaAdmin(admin.ModelAdmin):
    list_display=get_model_fields(Roznamcha)
    readonly_field=("spender",)
 
    def save_model(self,request,obj,form,change): 
        obj.user=request.user
        obj.save()
        

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

@admin.register(Asset)
class Initial_assetAdmin(admin.ModelAdmin):
    list_display=("initial_asset","current_asset","start_date") 

@admin.register(Sale_bill)
class SaleAdmin(admin.ModelAdmin):
    #list_display=get_model_fields(Sale_bill)  
    list_display=("payment","sale_date","seller","customer","total_sale_bill","discount")


@admin.register(Sales_detail)
class Sales_detailAdmin(admin.ModelAdmin):
    #list_display=get_model_fields(Sales_detail)   
    list_display=("sale_bill","product","item_amount","item_price","return_qty")

# @admin.register(Sale_bill)
# class SaleBillAdmin(admin.ModelAdmin):
#     #list_display=("customer","item_name","item_price","discount","amount","selling_date","total","paid","debit")
#     list_display=("sale_id","product_id","qty","pprice","sprice","return_qty")
    # def total(self,obj):
    #     return (obj.amount*obj.item_price)-obj.discount

    # def debit(self,obj): 
    #     return (obj.amount*obj.item_price)-obj.discount-obj.paid
        
             
