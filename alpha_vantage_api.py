# alpha_vantage_api.py
# This module provides a class for interacting with the Alpha Vantage API to fetch stock data.
# It includes methods to verify the API key, fetch daily time series data for a stock symbol,
# Author: Vendel, GITHUB: jv813yh
# Date: 08/01/2025

from http_client import HTTP_CLIENT_PROVIDER

API_KEY = 'F74BHY6LTAQHJ61K'

class AlphaVantageProvider:    
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = "https://www.alphavantage.co/query"

    def veryfy_api_key(self):
        """
        Verifies if the provided API key is valid by making a test request.
        Raises ValueError if the API key is empty."""
        if not self.api_key:
            raise ValueError("API key must not be empty")
        
    def verify_symbol(self, symbol):
        """
        Verifies if the provided stock symbol is valid by making a test request.
        Raises ValueError if the symbol is empty or invalid.
        """
        if not symbol:
            raise ValueError("Stock symbol must not be empty")
        


    def get_time_series_daily_data(self, symbol:str):
        """
        Fetches daily time series data for a given stock symbol from Alpha Vantage.
        """
        try:
            # Verify stock symbol
            self.verify_symbol(symbol)
        
            # Prepare parameters for the API request
            stock_params = {
                "function": "TIME_SERIES_DAILY",
                "symbol": symbol.upper(),
                "apikey": self.api_key
            }

            # Make the API request
            data_json = HTTP_CLIENT_PROVIDER.get(self.base_url, params=stock_params)
            
            if "Time Series (Daily)" in data_json:
                return data_json["Time Series (Daily)"]
            
            else:
                return data_json
        except Exception as e:
            raise ConnectionError(f"Failed to fetch data for {symbol}: {e}")
            