from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader 
from django.contrib.auth.decorators import login_required
from shopapp.models import Customer, Supplier , Supplier_Ledger , Customer_Ledger , Log ,Purchase_bill, Purchase_detail,Sale_bill,Sales_detail,Roznamcha,Asset
from products.models import Product
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib import messages

@login_required(login_url='/admin')
def roznamcha_form(request):  
    template=loader.get_template('roznamcha.html')
    #return HttpResponse(User.objects.all())
    context={
        'users':User.objects.all()
    } 
    return HttpResponse(template.render(context,request))
  
@login_required(login_url='/admin') 
def roznamcha_save(request): 
    print(request.POST)
    #return HttpResponse(request.POST)
    spender=request.POST['spender']
    total_spent=request.POST['total_spent']
    detail=request.POST['detail']
    date=datetime.now().strftime("%Y-%m-%d")
    #return HttpResponse(date)
    roznamcha=Roznamcha(spender=spender,total_spent=total_spent,detail=detail,date=date)
    try:
        roznamcha.save()
        messages.success(request,'روزنامچه ولیکل شوه')    
    except:
        
        messages.error(request,'روزنامچه ونه لیکل شوه')    
    return HttpResponseRedirect(reverse("roznamcha_form"))

