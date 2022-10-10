from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import VendorSerializer
from .models import Product,Vendors

@api_view(('GET','POST'))
def vendors_show(request,id="all"):
    print("id=",id)
    if id=="all":
        query_set=Vendors.objects.all().order_by('-pk')
    else:
        query_set=Vendors.objects.filter(id=int(id))

    serializer=VendorSerializer(query_set,many=True)

    return Response(serializer.data)




