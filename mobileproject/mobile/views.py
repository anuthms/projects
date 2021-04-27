from django.shortcuts import render,redirect
from mobile.forms import Brandcreateform,Mobilecreateform,Orderform
from .models import Brands,Mobile,Order
from .forms import Userregform,User
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.views.generic import TemplateView,CreateView,DetailView,DeleteView,ListView
# Create your views here.

def admin_permission_required(func):
    def wrapper(request):
        if not request.user.is_superuser:
            return redirect("errorpage")
        else:
            return func(request)
    return wrapper




def brand_view(request):
    brands=Brands.objects.all()
    form=Brandcreateform()
    context={}
    context["brands"]=brands
    context["form"]=form
    if request.method=="POST":
        form=Brandcreateform(request.POST)
    if form.is_valid():
        form.save()
        print("saved")
        return redirect("brandview")

    return render(request,"mobile/brand.html",context)



def error(request):
    return render(request,"mobile/errorpage.html")


def delete(request,id):
    brands=Brands.objects.get(id=id)
    brands.delete()
    return redirect("brandview")

def edit(request, id):
        brands = Brands.objects.get(id=id)
        form = Brandcreateform(instance=brands)
        context = {}
        context["form"] = form
        if request.method == "POST":
            form = Brandcreateform(request.POST,instance=brands)
        if form.is_valid():
            form.save()
            return redirect("brandview")
        return render(request, "mobile/brand.html", context)

def createmobile(request):
    form=Mobilecreateform()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=Mobilecreateform(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            print("saved")
            return redirect("createmobile")
    return render(request,"mobile/mobilecreate.html",context)

def listmobiles(request):
    mobiles=Mobile.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"mobile/listmobiles.html",context)

def mobiledetails(request,id):
    mobile=Mobile.objects.get(id=id)
    context={}
    context['mobile']=mobile
    return render(request,"mobile/mobiledetails.html",context)


def userregistration(request):
    form=Userregform()
    context={}
    context['form']=form
    if request.method=="POST":
        product=Userregform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("userlogin")
    return render(request,"mobile/userreg1.html",context)

def userlogin(request):
    if request.method=="POST":
        username=request.POST.get("uname")
        password=request.POST.get("pwd")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect("listmobiles")
        else:
            return render(request,"mobile/login.html")
    return render(request,"mobile/login.html")

def userlogout(request):
    logout(request)
    return redirect("userlogin")



def Order(request,id):
    product=Mobile.objects.get(id=id)
    form=Orderform(initial={'user':request.user,'product':product})
    context = {}
    context["form"] = form
    context["product"]=product
    if request.method == "POST":
       form = Orderform(request.POST)
       if form.is_valid():
           form.save()
           return redirect("cart")
       else:
           form=Orderform(request.POST)
           context['form']=form
           context['product']=product
           return render(request,"mobile/orders.html", context)
    return render(request,"mobile/orders.html", context)

def cart(request):
    username=request.user
    orders=Order.objects.all().filter(user=username)
    for order in orders:
        print(order.product,order.user,order.status)
    context={}
    context['orders']=orders
    return render(request,"mobile/cart.html",context)

class brands(TemplateView):
    model=Brands
    form_class= Brandcreateform
    template_name = "mobile/brand.html"
    context={}
    def get(self,request,*args,**kwargs):
        brands=self.model.objects.all()
        self.context["brands"]=brands
        return render(request,self.template_name,self.context)

class brand_delete(DeleteView):
    model=Brands
    template_name = "mobile/brand.html"
    context={}
    def get(self, request, *args, **kwargs):
        brands = self.model.objects.get(id=kwargs["id"])
        brands.delete()
        return redirect("brand")

class edit(TemplateView):
    model= Brands
    form_class= Brandcreateform
    template_name = "mobile/brand.html"
    context={}
    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self,request, *args,**kwargs):
        brands=self.model.objects.get(id=kwargs["id"])
        form=self.form_class(instance=brands)
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        brands = self.get_object(kwargs["id"])
        form = self.form_class(request.POST, instance=brands)
        if form.is_valid():
            form.save()
            return redirect("brand")
        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)

class createmobile(CreateView):
    model =Mobile
    form_class= Mobilecreateform
    template_name = "mobile/mobilecreate.html"
    context={}
    def get(self, request, *args, **kwargs):
        mobile = self.model.objects.get(id=kwargs["id"])
        form = self.form_class(instance=mobile)
        self.context["form"] = form
        return render(request, self.template_name, self.context)
    def post(self,request,*args,**kwargs):
        mobile = self.get_object(kwargs["id"])
        form = self.form_class(request.POST,instance=mobile)
        if form.is_valid():
            form.save()
            return redirect("createmobile")
        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)

class listmobiles(ListView):
    model=Mobile
    template_name = "mobile/listmobiles.html"
    context={}
    def get(self, request, *args, **kwargs):
        mobiles= self.model.objects.all()
        self.context["mobiles"] = mobiles
        return render(request, self.template_name, self.context)

class mobiledetails(DetailView):
    model = Mobile
    template_name = "mobile/mobiledetails.html"
    context={}
    def get(self, request, *args, **kwargs):
        mobile = self.model.objects.get(id=kwargs["id"])
        self.context["mobile"] = mobile
        return render(request, self.template_name, self.context)

class userregistration(TemplateView):
    model=Mobile
    form_class= Userregform
    template_name = "mobile/userreg1.html"
    context={}
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        self.context["form"] = form
        return render(request, self.template_name, self.context)
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("userlogin")
        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)

class userlogin(TemplateView):
    model=Mobile
    form_class=Userregform
    template_name = "mobile/login.html"
    context={}
    def get(self, request, *args, **kwargs):
        form =self.form_class()
        self.context["form"] = form
        return render(request, self.template_name, self.context)
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            self.context["form"] = form
            return redirect("listmobiles")

class Order(TemplateView):
    model=Order
    form_class=Orderform
    template_name = "mobile/order.html"
    context={}
    def get(self, request, *args, **kwargs):
        product= self.model.objects.get(id=kwargs["id"])
        self.context["product"] = product
        form=self.form_class(initial={'product':product,'user':request.user})
        self.context["form"]=form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = Orderform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cart")
        else:
            def get(self, request, *args, **kwargs):
                product = self.model.objects.get(id=kwargs["id"])
                self.context["product"] = product
                form = self.form_class(initial={'product': product, 'user': request.user})
                self.context["form"] = form
                return render(request, self.template_name, self.context)


class cart(TemplateView):
    model=Order
    template_name = "mobile/cart.html"
    context={}
    def get(self,request,*args,**kwargs):
        username=request.user
        orders=self.model.objects.all().filter(user=username)
        self.context["orders"]=orders
        return render(request, self.template_name, self.context)











