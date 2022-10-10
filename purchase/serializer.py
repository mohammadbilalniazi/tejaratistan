from rest_framework import serializers,response
from .models import Purchase_detail,Purchase_bill



class Purchase_detail_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Purchase_detail
        fields='__all__'
        fields=["id","product","item_amount","item_price","return_qty"]

class Purchase_bill_Serializer(serializers.ModelSerializer):
    purchase_detail_set = Purchase_detail_Serializer(many=True)
    class Meta:
        model=Purchase_bill
        fields=["id","purchase_detail_set","payment","purchasing_date","purchaser","seller","discount","total_purchase_bill"] #month===> kaifyath_haziri

    def create(self, validated_data):
        purchase_detail_set = validated_data.pop('purchase_detail_set')
        purchase_bill = Purchase_bill.objects.create(**validated_data)
        purchase_bill.save()
        for purchase_detail in purchase_detail_set:
            purchase_detail_obj = Purchase_detail.objects.create(purchase_bill=purchase_bill, **purchase_detail)
            purchase_detail_obj.save()
        return purchase_bill
