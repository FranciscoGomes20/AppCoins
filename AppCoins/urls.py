from django.urls import path
from .views import ( UserCreateView, LogoutView,
    CurrencyListCreateView, CurrencyDetailView, 
    ExchangeRateListCreateView, ExchangeRateDetailView, 
    ProfileListCreateView, ProfileDetailView, 
    TransactionListCreateView, TransactionDetailView,
    AlertSerializerCreateView, AlertDetailView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Para obter o token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Para atualizar o token
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='user-register'),
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
