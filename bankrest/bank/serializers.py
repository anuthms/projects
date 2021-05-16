from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from bank.models import Accounts


class UserRegSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

class AccountSerializer(ModelSerializer):
    class Meta:
        model=Accounts
        fields='__all__'


class TransactionSeraializer(serializers.Serializer):
    from_ac_num = serializers.CharField()
    to_ac_num = serializers.CharField()
    amount = serializers.IntegerField()
    debit_credit = serializers.CharField()


class DepositSerialiezer(serializers.Serializer):

    amount=serializers.IntegerField()

class WithdrawSerializer(serializers.Serializer):
    amount = serializers.IntegerField()