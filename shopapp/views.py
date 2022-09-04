from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader 
from django.contrib.auth.decorators import login_required
from shopapp.models import Customer, Supplier , Supplier_Ledger , Customer_Ledger , Log ,Purchase_bill, Purchase_detail,Sale_bill,Sales_detail,Roznamcha,Asset
from products.models import Product
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime


@login_required(login_url='/admin')
def index(request):
    template=loader.get_template('index.html') 
    return HttpResponse(template.render())

def bank_users(request):
    mymembers=Members.objects.all().values()
    template=loader.get_template('bank_users.html')

    context={  
        "bankmembers":mymembers
    }
    return HttpResponse(template.render(context,request))
    '''outputs=""
    for member in mymembers:
        outputs+="<h1>"+member["firstname"]+" "+"</h1>"
    return HttpResponse(outputs)'''  

def update_bank_user_form(request,id):
    template=loader.get_template('update_bank_users.html')
    member=Members.objects.get(id=id)
    
    context={
        "bank_user_by_id":member 
    }
    #return HttpResponse(member)
    return HttpResponse(template.render(context,request))

def update_bank_user(request,id):
    #return HttpResponse(request.POST.items())
    
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    member=Members.objects.get(id=id)
    member.firstname=first_name 
    member.lastname=last_name
    member.save()
    return HttpResponseRedirect(reverse('bankusers')) 



def delete_bank_user(request,id):
    user=Members.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse("bankusers"))

def salary(request):
    salary=Salary.objects.all().values()
    template=loader.get_template("salary.html")
    context={
        "bank_salaries":salary
    }
    #return HttpResponse(salary)
    return HttpResponse(template.render(context,request))

def home(request):
    template=loader.get_template("home.html")
    return HttpResponse(template.render())

def add_salary(request):
    template=loader.get_template("add_salary.html")
    return HttpResponse(template.render({},request))

def store_salary(request):
    account_no=request.POST['account_no']
    salary=request.POST['salary']
    sal_obj=Salary(account_no=account_no,amount=salary)
    sal_obj.save()
    return HttpResponseRedirect(reverse("index"))
 
# Create your views here.


def hawala_page(request):
    hawalas=Hawala.objects.all().order_by('sender').values()
    #hawala_rejected=Hawala.objects.filter(status='accepted',sender='thadiat')#hawala_rejected=Hawala.objects.filter(sender__startswith='t').values()
    
    #rows=len(hawala_rejected)
    
    context={
        'hawalas':hawalas
        #'rows':rows
    }
    template=loader.get_template("hawala.html")
    return HttpResponse(template.render(context,request))
