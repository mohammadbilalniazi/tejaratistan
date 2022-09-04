from django.db import models


class Request(models.Model):
    requester_name=models.CharField(max_length=30)
    requester_email=models.CharField(max_length=50)
    #request_date=models.CharField(max_length=30)
    def __str__(self):
        return self.requester_name
    
class Services(models.Model):
    service=models.CharField(max_length=30)
    #service_starter=models.CharField(max_length=30)
    request=models.ForeignKey(Request,on_delete=models.DO_NOTHING,null=True)
    #start_date=models.DateField()
    
    def __str__(self):
        return self.service

    
    
    