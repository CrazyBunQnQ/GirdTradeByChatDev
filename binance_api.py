'''
Module for interacting with Binance API.
'''
import requests
class BinanceAPI:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://api.binance.com"
    def fetch_klines(self, symbol, interval):
        url = f"{self.base_url}/api/v3/klines"
        params = {'symbol': symbol, 'interval': interval}
        response = requests.get(url, params=params)
        return response.json()
    def get_current_price(self, symbol):
        url = f"{self.base_url}/api/v3/ticker/price"
        params = {'symbol': symbol}
        response = requests.get(url, params=params)
        return float(response.json()['price'])