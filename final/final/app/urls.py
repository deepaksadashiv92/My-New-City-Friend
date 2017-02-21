"""
Definition of urls for DjangoWebProject12.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.reg, name='reg'),
    url(r'^Reg$', app.views.reg, name='reg'),
    url(r'^RegSuccess$', app.views.regsuccess, name='regsuccess'),
    url(r'^Subscribe$', app.views.subscribe, name='subscribe'),
    url(r'^Login1$', app.views.login1, name='login1'),
    url(r'^LoginFail$', app.views.loginfail, name='loginfail'),
    url(r'^Welcome', app.views.welcome, name='welcome'),
    url(r'^Welcome1', app.views.welcome1, name='welcome1'),
    url(r'^RaiseComplaints$', app.views.complaints, name='complaints'),
    url(r'^ComplaintSuccess$', app.views.complaintsuccess, name='complaintsuccess'),
    url(r'^ComplaintFail', app.views.complaintfail, name='complaintfail'),
    url(r'^CreateReq$', app.views.createreq, name='createreq'),
    url(r'^MyReq$', app.views.myreq, name='myreq'),
    url(r'^ReqSuccess$', app.views.reqsuccess, name='reqsuccess'),
    url(r'^RegSuccess1$', app.views.regsuccess1, name='regsuccess1'),
    url(r'^GetList$', app.views.getlist, name='getlist'),
    url(r'^Assign$', app.views.assign, name='assign'),
    url(r'^AssignSuccess$', app.views.assignsuccess, name='assignsuccess'),
    url(r'^AssignFail$', app.views.assignfail, name='assignfail'),
    url(r'^Close$', app.views.close, name='close'),
    url(r'^CloseSuccess$', app.views.closesuccess, name='closesuccess'),
    url(r'^CloseFail$', app.views.closefail, name='closefail'),
    url(r'^index$', app.views.home, name='home'),
    url(r'^home$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^LogOut', app.views.logout, name='logout'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
