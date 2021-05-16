"""restbank URL Configuration

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
from .views import UserRegistration,UserLogin,UserLogout,AccountCreate,Deposit,MoneyTransfer,Withdraw,BalanceCheck,TransactionHistory,CreditedHistory,DebitHistory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',UserRegistration.as_view()),
    path('login/',UserLogin.as_view()),
    path('logout/',UserLogout.as_view()),
    path('createacc/',AccountCreate.as_view()),
    path('deposit/<int:acc>',Deposit.as_view()),
    path('withdraw/<int:acc>',Withdraw.as_view()),
    path('money_transfer/',MoneyTransfer.as_view()),
    path('transaction/history/<int:acc>',TransactionHistory.as_view()),
    path('transaction/credithistory/<int:acc>',CreditedHistory.as_view()),
    path("transaction/debitedhistory/<int:acc>",DebitHistory.as_view()),
    path('balancecheck/<int:acc>',BalanceCheck.as_view()),
]
