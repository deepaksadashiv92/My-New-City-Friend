"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.widgets import AdminDateWidget

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
class Register(forms.Form):
    Cust_Name = forms.CharField(label=_("Name"))
    Cust_Password = forms.CharField(label=_("Password"),widget=forms.PasswordInput({
                                   'class': 'form-control'}))
    Cust_EmailID = forms.EmailField(label=_("Email ID"))
    Cust_Address = forms.CharField(label=_("Address"))
    Cust_PhoneNumber = forms.CharField(label=_("Phone Number"),max_length=10)
    Cust_DOB=forms.DateField(widget = forms.SelectDateWidget(years=range(2016,1930,-1)),label=_("Date of Birth"))
    CHOICES = (('1', 'Male',), ('2', 'Female',))
    Cust_Gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

class Login(forms.Form):
    Cust_EmailID = forms.EmailField(label=_("Email ID")) 
    Cust_Password = forms.CharField(label=_("Password"),widget=forms.PasswordInput({'class': 'form-control'}))

class Complaint(forms.Form):
    Req_ID=forms.CharField(label=_("Request ID"))
    Complaint_Description=forms.CharField(widget=forms.Textarea,label=_("Complaint Description"),max_length=1000)

class Request(forms.Form):
    OwnerName = forms.CharField(label=_("Owner Name"),required=True)
    Address = forms.CharField(label=_("Address"),required=True)
    Address1 = forms.CharField(label=_("Address 1"))
    Address2 = forms.CharField(label=_("Address 2"))
    Comments = forms.CharField(widget=forms.Textarea,label=_("Comments"),max_length=1000)
    City = forms.CharField(label=_("City"),required=True)
    State = forms.CharField(label=_("State"),required=True)
    Zipcode = forms.CharField(label=_("Zipcode"),required=True)
    OwnerPhoneNumber =forms.CharField(label=_("Owner's Phone Number"),max_length=10,required=True)
    OwnerEmailID = forms.EmailField(label=_("Owner's Email ID"),required=True)

class Assign(forms.Form):
    Req_ID=forms.CharField(label=_("Request ID"))

class Close(forms.Form):
    Req_ID=forms.CharField(label=_("Request ID"))

class Subscribe(forms.Form):
    Card=forms.CharField(label=_("Card Number"))
    CHOICES = (('1', 'Visa',), ('2', 'Mastercard',))
    Cardtype = forms.ChoiceField(label=_("Card Type"),choices=CHOICES)

    
                         

    
