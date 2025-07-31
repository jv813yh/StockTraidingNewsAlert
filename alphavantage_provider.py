import requests
import json


class AlphaVantageProvider:    
    def __init__(self, api_key):
        self.api_key = api_key
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
            response = requests.get(self.base_url, params=stock_params)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            
            if "Time Series (Daily)" in data:
                return data["Time Series (Daily)"]
            
            else:
                return data
            
        except requests.RequestException as e:
            raise ConnectionError("Failed to connect to Alpha Vantage API: " + str(e))
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON response from Alpha Vantage API")
        except Exception as e:
            raise Exception("An unexpected error occurred: " + str(e))