from django.shortcuts import render

# Create your views here.
def getcalc(request):
    return render(request,"calculation.html")

def solve(request):
    num1 = int(request.POST.get("num1"))
    num2 = int(request.POST.get("num2"))
    add=(num1+num2)
    context={}
    context['res']=add
    return render(request, "calculation.html",context)
