from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum,Count
from .models import Employee


# Create your views here.

def home(request):
    send_mail(request)
    sms_otp(request)
    url=request.build_absolute_uri('city')
    return render(request,'index.html',{'url':url})


def send_mail(request):
    print("send mail sucess")

def sms_otp(request):
    print("sms otp sending")


def employee_count(request):
    city_count=Employee.objects.values('city').annotate(city_count=Count('city')).order_by('city')
    return render(request,'employee.html',{'city':city_count})

def admin_register(request):
    pass
