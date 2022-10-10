from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader 
from django.contrib.auth.decorators import login_required
from shopapp.models import Customer, Supplier , Supplier_Ledger , Customer_Ledger , Log ,Sale_bill,Sales_detail,Roznamcha,Asset
from products.models import Product
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime


# @login_required(login_url='/admin')
def index(request):
    template=loader.get_template('index.html') 
    return HttpResponse(template.render())


