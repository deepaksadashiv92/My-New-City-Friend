"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .forms import Register,Login,Complaint,Request,Assign,Close,Subscribe
#importing forms
from .models import Customer,Complaints,Requests,RequestMgr
#importing models
import hashlib 
import sys
# it is the function for log in page which is validating from the form used and saving the data and also encrypting the password.
# the validation and the data objects used it taken from forms and models

def reg(request):
    assert isinstance(request, HttpRequest)
    if(request.method=="POST"):
        #post method
        f=Register(request.POST)
        if f.is_valid():
            Name=f.cleaned_data.get("Cust_Name")
            Password=f.cleaned_data.get("Cust_Password")
            EmailID=f.cleaned_data.get("Cust_EmailID")
            Address=f.cleaned_data.get("Cust_Address")
            PhoneNumber=f.cleaned_data.get("Cust_PhoneNumber")
            DOB=f.cleaned_data.get("Cust_DOB")
            Gender=f.cleaned_data.get("Cust_Gender")
            bPassword = Password.encode()
            e=hashlib.sha512()
            #password encryption
            e.update(bPassword)
            encrypted=e.digest()
            print(encrypted)
            try:
                print("Entered Try for Registration")
                #validation of the form and saving it
                c=Customer.objects.create(Cust_Name=Name,Cust_Password=encrypted,Cust_EmailID=EmailID,Cust_Address=Address,Cust_PhoneNumber=PhoneNumber,Cust_DOB=DOB,Cust_Gender=Gender,Cust_SubscriptionStatus="0")
                c.save()
                print(EmailID)
                return render(request,'app/RegSuccess.html')
            except:
                print("Unexpected error:", sys.exc_info())
                return render(request,'app/Reg.html',{'myForm':f})
        else:
            print("Error while registering")
            return render(request,'app/Reg.html')    
        #the get method used to get the login screen
    else:
        f=Register()
        return render(request,
        'app/Reg.html',{'myForm':f})

def regsuccess(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/RegSuccess.html'
        )

def regsuccess1(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/RegSuccess1.html'
        )
# a subscription page where the validation is checked for the user who has logged in
def subscribe(request):
    assert isinstance(request,HttpRequest)
    if request.method == 'POST':
        print('POST')
        f=Subscribe(request.POST)
        if f.is_valid():
                return render(request,'app/RegSuccess1.html')
        else:
                f=Subscribe()
                return render(request,'app/Subscribe.html',{'myForm':f})
    else:
        f=Subscribe()
        return render(request,'app/Subscribe.html',{'myForm':f})

def complaints(request):
     assert isinstance(request,HttpRequest)
     if request.method == 'POST':
        print('POST')
        f=Complaint(request.POST)
        if f.is_valid():
            EmailID=request.session['useremailid']
            ReqID=f.cleaned_data.get('Req_ID')
            Complaint_Desc=f.cleaned_data.get('Complaint_Description')
            r1=Requests.objects.filter(Req_ID=ReqID)
            if r1 :
                #getting the request data and saving it into the dataase
                c=Complaints.objects.create(Complaint_ID="0",Cust_EmailID=EmailID,Req_ID=ReqID,Complaint_Description=Complaint_Desc)
                c.save()
                c.Complaint_ID=c.id
                c.save
                print(EmailID)
                return render(request,'app/ComplaintSuccess.html',{'name':request.session['username'],'email':request.session['useremailid']})
            else:
                return render(request,'app/ComplaintFail.html',{'name':request.session['username'],'email':request.session['useremailid']})
        else:
            f=Complaint()
            return render(request,'app/RaiseComplaints.html',{'myForm':f,'name':request.session['username'],'email':request.session['useremailid']})
     else:
        f=Complaint()
        return render(request,'app/RaiseComplaints.html',{'myForm':f,'name':request.session['username'],'email':request.session['useremailid']})
# a complain get method file
def complaintsuccess(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/ComplaintSuccess.html',{'name':request.session['username'],'email':request.session['useremailid']}
        )

def complaintfail(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/ComplaintFail.html',{'name':request.session['username'],'email':request.session['useremailid']}
        )

def login1(request):
    assert isinstance(request, HttpRequest)
    if(request.method=="POST"):
        f=Login(request.POST)
        if f.is_valid():
         EmailID=f.cleaned_data.get("Cust_EmailID")
         Password=f.cleaned_data.get("Cust_Password")
         bPassword = Password.encode()
         e=hashlib.sha512()
         e.update(bPassword)
         encrypted=e.digest()
         try:
                print("Entered Try for Login")
                e1=Customer.objects.filter(Cust_EmailID=EmailID)
                if e1:
                    print("Email ID found")
                    for r in e1:
                       print(r.Cust_EmailID)
                       print("Original")
                       print(r.Cust_Password)
                       print("Encrypted")
                       print(encrypted)
                    #providing the expiry time for the login
                       request.session.set_expiry(1200)
                       request.session['username']=r.Cust_Name
                       request.session['useremailid']=r.Cust_EmailID
                        #validation check
                       if(r.Cust_Password == encrypted):
                          return render(request,'app/Welcome.html',{'myForm':Complaint(),'name':request.session['username'],'email':request.session['useremailid']})  
                       else:
                         return render(request,'app/LoginFail.html')
                else:
                    e2=RequestMgr.objects.filter(ReqMgr_EmailID=EmailID)
                    if e2:
                     print("Email ID for Req Mgr found")
                     for r in e2:
                       print(r.ReqMgr_EmailID)
                       print("Original")
                       print(r.ReqMgr_Password)
                       print("Encrypted")
                       print(encrypted)
                       request.session.set_expiry(1200)
                       request.session['username']=r.ReqMgr_Name
                       request.session['useremailid']=r.ReqMgr_EmailID
                       if(r.ReqMgr_Password == encrypted):
                          return render(request,'app/Welcome1.html',{'name':request.session['username'],'email':request.session['useremailid']})  
                       else:
                         return render(request,'app/LoginFail.html')
                    return render(request,'app/LoginFail.html')
         except:
                print("Unexpected error:", sys.exc_info())
                return render(request,'app/LoginFail.html')
        else:
            return render(request,'app/LoginFail.html')                   
    else:
        print("Entered GET for Login")
        f=Login()
        return render(
        request,
        'app/Login1.html',{'myForm':f})

def loginfail(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/LoginFail.html'
        )

def logout(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/LogOut.html')

def welcome(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Welcome.html',{'name':request.session['username'],'email':request.session['useremailid']}
        )

def welcome1(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Welcome1.html',{'name':request.session['username'],'email':request.session['useremailid']}
        )

def createreq(request):
    assert isinstance(request, HttpRequest)
    if(request.method=="POST"):
        f=Request(request.POST)
        if f.is_valid():
            fOwnerName = f.cleaned_data.get("OwnerName")
            fAddress = f.cleaned_data.get("Address")
            fAddress1 = f.cleaned_data.get("Address1")
            fAddress2 = f.cleaned_data.get("Address2")
            fComments = f.cleaned_data.get("Comments")
            fCity = f.cleaned_data.get("City")
            fState = f.cleaned_data.get("State")
            fZipcode = f.cleaned_data.get("Zipcode")
            fOwnerPhoneNumber = f.cleaned_data.get("OwnerPhoneNumber")
            fOwnerEmailID = f.cleaned_data.get("OwnerEmailID")
            try:
                print("Entered Try for Request Creation")
                c=Requests.objects.create(OwnerName=fOwnerName,Address=fAddress,Address1=fAddress1,Address2=fAddress2,Comments=fComments,City=fCity,State=fState,Zipcode=fZipcode,OwnerPhoneNumber=fOwnerPhoneNumber,OwnerEmailID=fOwnerEmailID,ReqMgr_EmailID="NULL@NULL.com",CloseComments="NULL",Req_ID="0",Cust_EmailID=request.session['useremailid'])
                c.save()
                c.Req_ID=c.id
                c.save()
                print(c.Req_ID)
                return render(request,'app/ReqSuccess.html',{'name':request.session['username'],'email':request.session['useremailid']})
            except:
                print("Unexpected error:", sys.exc_info())
                return render(request,'app/CreateReq.html',{'myForm':Request(),'name':request.session['username'],'email':request.session['useremailid']})
        else:
            print("Error while registering")
            return render(request,'app/CreateReq.html',{'myForm':Request(),'name':request.session['username'],'email':request.session['useremailid']})                   
    else:
        return render(
        request,
        'app/CreateReq.html',{'myForm':Request(),'name':request.session['username'],'email':request.session['useremailid']})

def reqsuccess(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/ReqSuccess.html',{'name':request.session['username'],'email':request.session['useremailid']}
        )

def myreq(request):
    assert isinstance(request, HttpRequest)
    query_results = Requests.objects.filter(Cust_EmailID=request.session['useremailid'])
    if query_results:
      print("Entered if of myreq")
      return render(
        request,
        'app/MyReq.html',{'query_results':query_results,'name':request.session['username'],'email':request.session['useremailid']})
    else:
        return render(
        request,
        'app/MyReq.html',{'query_results':query_results,'name':request.session['username'],'email':request.session['useremailid']})

def getlist(request):
    assert isinstance(request, HttpRequest)
    query_results = Requests.objects.all()
    if query_results:
      print("Entered if of myreq")
      return render(
        request,
        'app/GetList.html',{'query_results':query_results,'name':request.session['username'],'email':request.session['useremailid']})
    else:
        return render(
        request,
        'app/GetList.html',{'query_results':query_results,'name':request.session['username'],'email':request.session['useremailid']})

def assign(request):
     assert isinstance(request,HttpRequest)
     if request.method == 'POST':
        print('POST')
        f=Assign(request.POST)
        if f.is_valid():
            ReqID=f.cleaned_data.get('Req_ID')
            r1=Requests.objects.filter(Req_ID=ReqID)
            if r1:
              r1.update(ReqMgr_EmailID=request.session['useremailid'])
              return render(request,'app/AssignSuccess.html',{'name':request.session['username'],'email':request.session['useremailid']})
            else:
              return render(request,'app/AssignFail.html',{'name':request.session['username'],'email':request.session['useremailid']})
        else:
            return render(request,'app/AssignFail.html',{'name':request.session['username'],'email':request.session['useremailid']})
     else:
        f=Assign()
        return render(request,'app/Assign.html',{'myForm':f,'name':request.session['username'],'email':request.session['useremailid']})


def assignsuccess(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/AssignSuccess.html',{'name':request.session['username'],'email':request.session['useremailid']}
        )

def assignfail(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/AssignFail.html',{'name':request.session['username'],'email':request.session['useremailid']})
        
def close(request):
     assert isinstance(request,HttpRequest)
     if request.method == 'POST':
        print('POST')
        f=Close(request.POST)
        if f.is_valid():
            ReqID=f.cleaned_data.get('Req_ID')
            r1=Requests.objects.filter(Req_ID=ReqID)
            if r1:
              r1.delete()
              return render(request,'app/CloseSuccess.html',{'name':request.session['username'],'email':request.session['useremailid']})
            else:
              return render(request,'app/CloseFail.html',{'name':request.session['username'],'email':request.session['useremailid']})
        else:
            return render(request,'app/CloseFail.html',{'name':request.session['username'],'email':request.session['useremailid']})
     else:
        f=Close()
        return render(request,'app/Close.html',{'myForm':f,'name':request.session['username'],'email':request.session['useremailid']})


def closesuccess(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/CloseSuccess.html',{'name':request.session['username'],'email':request.session['useremailid']}
        )

def closefail(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/CloseFail.html',{'name':request.session['username'],'email':request.session['useremailid']}
        )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )
