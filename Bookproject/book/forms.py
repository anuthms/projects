from django import forms
from django.forms import ModelForm
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# class Bookcreateform(forms.Form):
#     book_name = forms.CharField(max_length=120)
#     author = forms.CharField(max_length=120)
#     price = forms.IntegerField()
#     pages = forms.IntegerField()
#     category = forms.CharField(max_length=120)

class Bookcreateform(ModelForm):
    class Meta:
        model=Book
        fields='__all__'
        widgets={
            'book_name':forms.TextInput(attrs={'class':'form-control'})
        }



    def clean(self):
        cleaned_data=super().clean()
        price=cleaned_data.get("price")

        if price<0:
            msg = "invalid price please provide valid price"
            self.add_error("price",msg)

class Bookupdateform(ModelForm):
    class Meta:
        model=Book
        fields='__all__'


class UserRegForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

class loginform(forms.Form):
    username=forms.CharField(max_length=120)
    password=forms.CharField(widget=forms.PasswordInput)