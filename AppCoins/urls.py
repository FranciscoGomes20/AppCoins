from django.urls import path
from .views import (
    CurrencyListCreateView, CurrencyDetailView, 
    ExchangeRateListCreateView, ExchangeRateDetailView, 
    ProfileListCreateView, ProfileDetailView, 
    TransactionListCreateView, TransactionDetailView,
    AlertSerializerCreateView, AlertDetailView
)

urlpatterns = [
    path('currency/', CurrencyListCreateView.as_view(), name='currency-list-create'),
    path('currency/<int:pk>/', CurrencyDetailView.as_view(), name='currency-detail'),
    path('exchangerate/', ExchangeRateListCreateView.as_view(), name='exchangerate-list-create'),
    path('exchangerate/<int:pk>/', ExchangeRateDetailView.as_view(), name='exchangerate-detail'),
    path('profile/', ProfileListCreateView.as_view(), name='profile-list-creat'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('transaction/', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('transaction/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('alert/', AlertSerializerCreateView.as_view(), name='alert-list-creat'),
    path('alert/<int:pk>/', AlertDetailView.as_view(), name='alert-detail')
]
