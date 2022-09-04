from django.contrib import admin
from .models import Product
# Register your models here.
@admin.register(Product) 
class ProductAdmin(admin.ModelAdmin):
    
    list_display=("item_name","detail","minimum_requirement","item_amount_available","row","column")
    #list_display=get_model_fields(Product)
 
