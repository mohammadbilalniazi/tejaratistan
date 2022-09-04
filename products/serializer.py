from rest_framework import serializers,response
from .models import Product

class ProductSerializer(serializers.ModelSerializer): #serializers.ModelSerializer
    class Meta:
        model = Product
        fields ="__all__"

