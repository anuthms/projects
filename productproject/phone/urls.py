"""productproject URL Configuration

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
from .views import *
from django.shortcuts import render
urlpatterns = [
path("",lambda request:render(request,"mobile/index.html")),
     path("brands",Brand.as_view(),name="brand"),
    path("delete/<int:id>",brand_detele.as_view(),name="brand_delete"),
    path("edit/<int:id>",edit.as_view() , name="edit"),
    path("mobile", createmobile.as_view(), name="createmobile"),
    path("mobile/list", listmobiles.as_view(), name="listmobiles"),
    path("mobile/details/<int:id>", mobiledetails.as_view(), name="details"),
    path("mobile/userregistration", userregistration.as_view, name="register"),
    path("mobile/userlogin", userlogin.as_view(), name="userlogin"),
    path("mobile/userlogout", userlogout, name="userlogout"),

]
