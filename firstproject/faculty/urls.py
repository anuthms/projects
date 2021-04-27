"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from faculty.views import fac_login,fac_register,viewfac_feedback,viewfac_schedule,registration


urlpatterns = [
    path('register', fac_register,name="register"),
    path('post_feedback', viewfac_feedback,name="feedback"),
    path('login', fac_login, name="login"),
    path('view_schedule', viewfac_schedule,name="schedule"),
    path('signup',registration,name="signup")

]
