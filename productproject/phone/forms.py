from django.forms import ModelForm
from mobile.models import Brands,Mobile,Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Brandcreateform(ModelForm):
    class Meta:
        model=Brands
        fields="__all__"

class Mobilecreateform(ModelForm):
     class Meta:
         model=Mobile
         fields="__all__"



class Userregform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']




class Orderform(ModelForm):
    class Meta:
        model=Order
        fields="__all__"
