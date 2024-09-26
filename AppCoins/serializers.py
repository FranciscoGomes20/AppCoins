from rest_framework import serializers
from .models import Currency, ExchangeRate, Profile, Transaction, Alert

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['currency_code', 'currency_name', 'symbol']

class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = ['base_currency', 'target_currency', 'exchange_rate', 'rate_date']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        models = Profile
        fields = ['user', 'account_type']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['user', 'base_currency', 'target_currency', 'amount', 'converted_amount', 'transaction_date']

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ['user', 'base_currency', 'target_currency', 'target_rate', 'notified_at']
