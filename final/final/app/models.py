"""
Definition of models.
"""

from django.db import models

class Customer(models.Model):
    Cust_Name = models.CharField(max_length=50)
    Cust_Password = models.BinaryField(max_length=512)
    Cust_EmailID = models.EmailField(unique=True)
    Cust_Address = models.CharField(max_length=100)
    Cust_PhoneNumber = models.CharField(max_length=10)
    Cust_DOB = models.DateField()
    Cust_Gender = models.CharField(max_length=20)
    Cust_SubscriptionStatus = models.CharField(max_length=1)

class Complaints(models.Model):
    Complaint_ID = models.CharField(max_length=5,default="0")
    Req_ID = models.CharField(max_length=5,default="0")
    Cust_EmailID = models.EmailField()
    Complaint_Description = models.CharField(max_length=1000)

class Requests(models.Model):
    Req_ID = models.CharField(max_length=5,default="0")
    ReqMgr_EmailID= models.EmailField()
    Cust_EmailID = models.EmailField()
    OwnerName = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    Address1 = models.CharField(max_length=100)
    Address2 = models.CharField(max_length=100)
    Comments = models.CharField(max_length=1000)
    City = models.CharField(max_length=10)
    State = models.CharField(max_length=10)
    Zipcode = models.CharField(max_length=5)
    OwnerPhoneNumber = models.CharField(max_length=10)
    OwnerEmailID = models.EmailField()
    CloseComments=models.CharField(max_length=1000)

class RequestMgr(models.Model):
    ReqMgr_Name = models.CharField(max_length=50)
    ReqMgr_Password = models.BinaryField(max_length=512)
    ReqMgr_EmailID = models.EmailField(unique=True)
    ReqMgr_Address = models.CharField(max_length=100)
    ReqMgr_PhoneNumber = models.CharField(max_length=10)
    ReqMgr_DOB = models.DateField()
    ReqMgr_Gender = models.CharField(max_length=20)



    


# Create your models here.
