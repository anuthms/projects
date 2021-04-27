from .models import Mobile,Brands
from .forms import Brandcreateform,Userregform,Mobilecreateform
from django.shortcuts import redirect,render
from django.contrib.auth import logout,login

from django.views.generic import TemplateView,ListView,DetailView,CreateView
class Brands(TemplateView):
    model=Brands
    form_class= Brandcreateform
    template_name = "mobile/brand.html"
    context={}
    def get(self,request,*args,**kwargs):
        brands=self.model.objects.all()
        self.context["brands"]=brands
        return render(request,self.template_name,self.context)

class brand_detele(TemplateView):
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
        form = self.form_class()
        self.context["form"] = form
        return render(request, self.template_name, self.context)
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listmobiles")
        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)

def userlogout(request):
    logout(request)
    return redirect("userlogin")

