from django import forms

class studentregform(forms.Form):
    name = forms.CharField(max_length=126)
    email = forms.EmailField()
    course = forms.CharField(max_length=126)
    phone = forms.CharField(max_length=12)
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=120)
    def clean(self):
        print("inside clean")

class studentloginform(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(max_length=120)
    def clean(self):
        print("inside clean")
