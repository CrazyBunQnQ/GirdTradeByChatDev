'''
Module to handle interactions with the Binance API.
'''
import requests
class BinanceAPI:
    def __init__(self, api_key, api_secret):
        self.base_url = 'https://api.binance.com'
        self.api_key = api_key
        self.api_secret = api_secret
        self.headers = {'X-MBX-APIKEY': self.api_key}
    def get_account_info(self):
        """Retrieve account information from Binance."""
        url = f'{self.base_url}/api/v3/account'
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    def get_price(self, symbol):
        """Get latest price of a symbol."""
        url = f'{self.base_url}/api/v3/ticker/price?symbol={symbol}'
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return float(response.json()['price'])
    def place_order(self, symbol, side, quantity):
        """Place an order on Binance."""
        data = {
            'symbol': symbol,
            'side': side,
            'type': 'MARKET',
            'quantity': quantity,
        }
        url = f'{self.base_url}/api/v3/order'
        response = requests.post(url, headers=self.headers, data=data)
        response.raise_for_status()
        return response.json()