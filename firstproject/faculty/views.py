from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def fac_register(request):
    return HttpResponse("<h1>welcome to faculty registration</h1>")

def fac_login(request):
    return render(request,"faculty/fac_login.html")

def registration(request):
    name=request.POST.get("name")
    email=request.POST.get("email")
    password=request.POST.get("password")
    print(name,email,password)
    return render(request,"faculty/fac_login.html")

def viewfac_schedule(request):
    return HttpResponse("<h1>view schedule</h1>")

def viewfac_feedback(request):
    return HttpResponse("<h1>feedback</h1>")
