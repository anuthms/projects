"""mobileproject URL Configuration

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

from django.urls import path,include
from django.shortcuts import render
from .views import *
urlpatterns = [
    path("error", error, name="errorpage"),
    path("",lambda request:render(request,"mobile/index.html")),
    path("brands",brands.as_view(),name="brandview"),
    path("delete/<int:id>",brand_delete.as_view(),name="delete"),
    path("edit/<int:id>",edit.as_view(),name="edit"),
    path("mobiles",createmobile.as_view(),name="createmobile"),
    path("mobiles/list",listmobiles.as_view(),name="listmobiles"),
    path("mobiles/details/<int:id>",mobiledetails.as_view(),name="details"),
    path("mobiles/userregistration",userregistration.as_view(),name="register"),
    path("mobiles/userlogin",userlogin.as_view(),name="userlogin"),
    path("mobiles/userlogout",userlogout,name="userlogout"),
    path("Order/<int:id>",Order.as_view(),name="Order"),
    path("mobiles/cart",cart.as_view(),name="cart"),


]
