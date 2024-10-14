import os
from dotenv import load_dotenv
import requests

load_dotenv()

class FixerService:
    BASE_URL = "http://data.fixer.io/api/"
    API_KEY = os.getenv('API_KEY')

    @staticmethod
    def get_exchange_rates(base_currency='EUR', symbols=None):
        url = f"{FixerService.BASE_URL}latest"

        params = {
            'access_key': FixerService.API_KEY,
            'base': base_currency,  # Base currency (Fixer.io usa EUR como padrão, mas versões pagas permitem alterar)
            'symbols': ','.join(symbols) if symbols else None,  # Moedas específicas
        }

        response = requests.get(url, params=params)
        data = response.json()
        
        if response.status_code == 200 and data.get('success'):
            return data['rates']
        else:
            # Tratamento de erro
            raise Exception(f"Erro ao buscar taxas de câmbio: {data.get('error', 'Desconhecido')}")
