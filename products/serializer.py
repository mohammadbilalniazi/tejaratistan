from rest_framework import serializers,response
from .models import Product, Vendors ,Service , SubService



class ProductSerializer(serializers.ModelSerializer): #serializers.ModelSerializer
    class Meta:
        model = Product
        fields ="__all__"

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendors
        fields="__all__"


class SubServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubService
        fields=["service","sub_service_name","detail","html_id","is_active"]


# SubService=("service","detail","html_id","is_active")
# Service=("service_name","category","detail","html_id","service_incharger","is_active")
#     
class ServiceSerializer(serializers.ModelSerializer):
    subservice_set=SubServiceSerializer(many=True)
    class Meta:
        model=Service
        fields=["subservice_set","service_name","category","detail","html_id","service_incharger","is_active"]
