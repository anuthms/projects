

# Create your views here.
from .forms import Bookcreateform,Bookupdateform
from django.shortcuts import render,redirect
from .models import Book
from .forms import UserRegForm,loginform
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DetailView,DeleteView
from django.urls import reverse_lazy
def book_create(request):
    form=Bookcreateform()
    context={}
    context["form"]=form
    books=Book.objects.all()
    context["books"]=books
    if request.method == "POST":
      form=Bookcreateform(request.POST)
      if form.is_valid():
             # book_name= form.cleaned_data.get("book_name")
             # author=form.cleaned_data.get("author")
             # price=form.cleaned_data.get("price")
             # pages=form.cleaned_data.get("pages")
             # category=form.cleaned_data.get("category")
             # books=Book(book_name=book_name,author=author,price=price,pages=pages,category=category)
             # books.save()
             form.save()
             print("book object saved")
             return redirect("create")
      else:
          form=Bookcreateform(request.POST)
          context["form"]=form
          return render(request, "book/boolcreate.html", context)

    return render(request,"book/boolcreate.html",context)

def book_delete(request,id):
    books=Book.objects.get(id=id)
    books.delete()
    return redirect("create")


def book_view(request,id):
    book=Book.objects.get(id=id)
    context={}
    context["book"]=book
    return render(request,"book/bookdetail.html",context)


def book_update(request,id):
        book=Book.objects.get(id=id)
        form=Bookupdateform(instance=book)
        context={}
        context["form"]=form
        if request.method=="POST":
            form=Bookupdateform(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect("create")
        return render(request,"book/update.html",context)

def reg(request):
    form=UserRegForm()
    context={}
    context['form']=form
    if request.method=="POST":
        form=UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"book/login.html")
        else:
            form=UserRegForm(request.POST)
            context['form']=form
            return render(request, "book/register.html", context)


    return render(request,"book/register.html",context)

def login(request):
    form=loginform()
    context={}
    context['form']=form
    if request.method=="POST":
        form=loginform(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                print("login sucess")

                return redirect("create")
            else:
                print("failed")
                return render(request,"book/login.html",context)

    return render(request,"book/login.html",context)

#listing all books
class Books(TemplateView):
    model = Book
    template_name = "book/boolcreate.html"
    context={}
    def get(self,request, *args,**kwargs):
        books=self.model.objects.all()
        self.context["books"]=books
        return render(request,self.template_name,self.context)


#get method and post method

class Bookcreate(TemplateView):
    model=Book
    form_class =Bookcreateform
    template_name = "book/boolcreate.html"
    context={}
    def get(self,request,*args,**kwargs):
        self.context["form"]=self.form_class()
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clslist")
        else:
            self.context["form"]=form
            return render(request,self.template_name,self.context)

class Bookupdateview(TemplateView):
    model=Book
    form_class = Bookcreateform
    template_name = "book/update.html"
    context={}
    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self,request, *args,**kwargs):
        book=self.model.objects.get(id=kwargs["pk"])
        form=self.form_class(instance=book)
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        book = self.get_object(kwargs["pk"])
        form=self.form_class(request.POST,instance=book)
        if form.is_valid():
           form.save()
           return redirect("clslist")
        else:
            self.context["form"]=form
            return render(request, self.template_name, self.context)


class detailview(DetailView):
    model=Book
    template_name = "book/bookdetail.html"
    context={}
    def get(self,request,*args,**kwargs):
        book=self.model.objects.get(id=kwargs["pk"])
        self.context["book"]=book
        return render(request,self.template_name,self.context)

class deteleview(TemplateView):
    model=Book
    template_name = "book/bookdelete.html"
    context={}
    def get(self, request, *args, **kwargs):
        book = self.model.objects.get(id=kwargs["pk"])
        book.delete()
        return redirect("clslist")


