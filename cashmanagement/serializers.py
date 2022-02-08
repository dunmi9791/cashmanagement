from rest_framework import serializers
from .models import Account, Inflow


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('name', 'account_type', 'active', 'iban')


class InflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inflow
        fields = ('amount', 'date', 'type')
