from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CurrencySerializer, ExchangeRateSerializer, ProfileSerializer, TransactionSerializer, AlertSerializer, UserSerializer
from .models import Currency, ExchangeRate, Profile, Transaction, Alert
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .services import FixerService
from rest_framework import status
from decimal import Decimal

# Create your views here.
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            if refresh_token is None:
                return Response({"error": "Refresh token não fornecido"}, status=400)
            
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message": "Logout realizado com sucesso"}, status=200)
        except Exception as e:
            return Response({"error": f"Falha no logout: {str(e)}"}, status=400)

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class CurrencyListCreateView(ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [IsAuthenticated]

class CurrencyDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [IsAuthenticated]

class ExchangeRateListCreateView(ListCreateAPIView):
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer
    permission_classes = [IsAuthenticated]

class ExchangeRateDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer
    permission_classes = [IsAuthenticated]

class ProfileListCreateView(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

class ProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

class TransactionListCreateView(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            base_currency = serializer.validated_data['base_currency']
            target_currency = serializer.validated_data['target_currency']
            amount = serializer.validated_data['amount']

            try:
                exchange_rate = FixerService.get_exchange_rates(
                    base_currency=base_currency.currency_code,
                    symbols=[target_currency.currency_code]
                )[target_currency.currency_code]

                if exchange_rate is None:
                    return Response({'error': 'Taxa de câmbio não encontrada.'}, status=status.HTTP_400_BAD_REQUEST)
                
                if not isinstance(exchange_rate, (int, float)) or exchange_rate <= 0:
                    return Response({'error': 'Taxa de câmbio inválida.'}, status=status.HTTP_400_BAD_REQUEST)

                exchange_rate = Decimal(str(exchange_rate))

                # Calcula o valor convertido
                converted_amount = amount * exchange_rate
                
                # Cria a transação
                transaction = Transaction.objects.create(
                    user=request.user,
                    amount=amount,
                    base_currency=base_currency,
                    target_currency=target_currency,
                    converted_amount=converted_amount
                )
                
                return Response(TransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error!': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

class AlertSerializerCreateView(ListCreateAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [IsAuthenticated]

class AlertDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [IsAuthenticated]
