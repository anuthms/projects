from django.shortcuts import render
# from django.http import HttpResponse
#
# def stud_register(request):
#     return  render(request,"student/stud_register.html")
# def prime(request):
#     return render(request,'math/prime.html')
# def primeno(request):
#     num = int(request.POST.get("input"))
#     c = 0
#     for i in range(2, num):
#         if (num % i==0):
#             c = c + 1
#         else:
#             pass
#     if(c==0):
#         print("is prime")
#     else:
#         print("not prime")
#     return render(request,'math/prime.html')
#
#
# def registration(request):
#     name=request.POST.get("name")
#     email=request.POST.get("email")
#     password=request.POST.get("password")
#     print(name,email,password)
#     return render(request,"student/stud_login.html")
#
# def stud_login(request):
#     return render(request,"student/stud_login.html")
#
# def view_timetable(request):
#     return HttpResponse("<h1>view timetable</h1>")
#
# def post_feedback(request):
#     return HttpResponse ("<h1>feedback</h1>")
#
#
from student.forms import studentregform,studentloginform
def register(request):
    form=studentregform()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=studentregform(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email=form.cleaned_data.get("email")
            phone=form.cleaned_data.get("phone")
            print(name,"=>",email,"=>",phone)
            return render(request,"student/stud_register.html",context)


    return render(request,"student/stud_register.html",context)

def login_view(request):
    form=studentloginform()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=studentregform(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            print(username, "=>", password)
            return render(request, "student/stud_login.html", context)

    return render(request, "student/stud_login.html", context)
