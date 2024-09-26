from django.contrib import admin
from .models import Currency, ExchangeRate, Profile, Transaction, Alert

# Register your models here.
@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('currency_code', 'currency_name', 'symbol')
    search_fields = ('currency_code', 'currency_name')

@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('base_currency', 'target_currency', 'exchange_rate', 'rate_date')
    search_fields = ('base_currency', 'target_currency')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'account_type')
    search_fields = ('user', 'account_type')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'base_currency', 'target_currency', 'amount', 'converted_amount', 'transaction_date')
    search_fields = ('user', 'transaction_date')

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('user', 'base_currency', 'target_currency', 'target_rate', 'notified_at')
    search_fields = ('user', 'base_currency')
