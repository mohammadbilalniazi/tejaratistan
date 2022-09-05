"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shopapp import views,views_roznamcha,views_selling,views_purchase
from products import views as product_view
from user_requests import request_views
# from qrapp import views_qr 
    
urlpatterns = [
    path('admin/shopapp/roznamcha/add/',views_roznamcha.roznamcha_form,name='roznamcha_form'), 
    path('roznamcha/save',views_roznamcha.roznamcha_save),
    path('admin/shopapp/selling/add/',views_selling.selling_form,name='selling_form'),
    path('selling/save',views_selling.selling_save),
    path('admin/shopapp/purchase_bill/add/',views_purchase.purchase_bill_form,name="purchase_bill_form"),
    path('admin/shopapp/purchase_bill/',views_purchase.purchase_show),
    path('purchase_bill/detail/<purchase_bill_id>/',views_purchase.purchase_show),

    path('products/<id>/',product_view.show,name='product_show'),
#     path('qrapp/qr_generater/',views_qr.qr_generater),
#     path('qrapp/qr_reader/',views_qr.qr_reader),
    path('requests_user/request/save/',request_views.request),
    path('admin/', admin.site.urls),

    path('',views.index)
]
 
