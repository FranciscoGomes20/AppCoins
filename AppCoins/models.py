from django.db import models
from django.contrib.auth.models import User

class AuditModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="%(class)s_created_by", on_delete=models.SET_NULL, null=True)
    modified_by = models.ForeignKey(User, related_name="%(class)s_modified_by", on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True

class Currency(AuditModel): # Moedas ex: USD/EUR - US Dollar/Euro - $, €
    currency_code = models.CharField(max_length=3)
    currency_name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=5) 

    def __str__(self):
        return self.currency_code

class ExchangeRate(AuditModel): # Taxas de Câmbio 
    base_currency = models.ForeignKey(Currency, related_name='base_currency_rates', on_delete=models.CASCADE)
    target_currency = models.ForeignKey(Currency, related_name='target_currency_rates', on_delete=models.CASCADE)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=6)
    rate_date = models.DateTimeField()

    def __str__(self):
        return f"{self.base_currency} -> {self.target_currency} : {self.exchange_rate}"

class Profile(AuditModel): # Usuários padrão do Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=20, choices=[('free', 'Free'), ('premium', 'Premium')])

    def __str__(self):
        return self.user.username

class Transaction(AuditModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    base_currency = models.ForeignKey(Currency, related_name='base_currency_transactions', on_delete=models.CASCADE)
    target_currency = models.ForeignKey(Currency, related_name='target_currency_transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    converted_amount = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction by {self.user.username} from {self.base_currency} to {self.target_currency}"

class Alert(AuditModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    base_currency = models.ForeignKey(Currency, related_name='base_currency_alerts', on_delete=models.CASCADE)
    target_currency = models.ForeignKey(Currency, related_name='target_currency_alerts', on_delete=models.CASCADE)
    target_rate = models.DecimalField(max_digits=10, decimal_places=6)
    notified_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Alert for {self.user.username} - {self.base_currency} to {self.target_currency}"
