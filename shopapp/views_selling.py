from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader 
from django.contrib.auth.decorators import login_required
from shopapp.models import Customer, Supplier , Supplier_Ledger , Customer_Ledger , Log,Sale_bill,Sales_detail,Roznamcha,Asset
from products.models import Product
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime

@login_required(login_url='/admin')
def selling_form(request):  
    template=loader.get_template('selling.html')
    #return HttpResponse(User.objects.all())
    context={
        'customers':Customer.objects.all(),
        'products':Product.objects.all(),
    } 
    return HttpResponse(template.render(context,request))
  
@login_required(login_url='/admin') 
def selling_save(request): 
    #print(request.POST)
    #return HttpResponse(request.POST)
    customer=request.POST['customer']
    customer_id=Customer.objects.get(name=customer)
    #return HttpResponse(customer_id)
    item_name=request.POST['item_name']
    item_name=Product.objects.get(item_name=item_name)
    item_price=request.POST['item_price']
    discount=request.POST['discount']
    amount=request.POST['amount']
    paid=request.POST['paid']
    debit=request.POST['debit']
    selling_date=datetime.now().strftime("%Y-%m-%d")
    #return HttpResponse(date)
    #total=item_price*item_amount-discount-paid

    roznamcha=Selling(customer=customer_id,item_name=item_name,item_price=item_price,discount=discount,amount=amount,paid=paid,debit=debit,selling_date=selling_date)
    try:
        roznamcha.save()
        messages.success(request,'خرڅلاو ولیکل شو')    
    except:
        messages.error(request,'خرڅلاو ونه لیکل شو')
    return HttpResponseRedirect(reverse("selling_form"))

