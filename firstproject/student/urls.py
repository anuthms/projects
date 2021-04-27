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
from django.urls import path
from student.views import register,login_view
urlpatterns = [
    # path('register', stud_register,name="register"),
    # path('post_feedback',post_feedback,name="feedback"),
    # path('login',stud_login,name="login"),
    # path('view_timetable',view_timetable,name="timetable"),
    # path('signup',registration,name="signup"),
    # path('primeno',primeno,name="primeno"),
    # path('prime',prime,name="prime"),
    path("register",register,name="register"),
    path("login",login_view,name="login")






]
