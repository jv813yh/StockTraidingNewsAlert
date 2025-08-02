# alpha_vantage_api.py
# This module provides a class for interacting with the Alpha Vantage API to fetch stock data.
# It includes methods to verify the API key, fetch daily time series data for a stock symbol,
# Author: Vendel, GITHUB: jv813yh
# Date: 08/01/2025

from http_client import HTTP_CLIENT_PROVIDER
import datetime

API_KEY = 'F74BHY6LTAQHJ61K'
SATURDAY = 5
SUNDAY = 6

class AlphaVantageProvider:    
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = "https://www.alphavantage.co/query"

    def get_time_series_daily_data(self, symbol:str):
        """
        Fetches daily time series data for a given stock symbol from Alpha Vantage.
        """
        try:

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


if __name__ == "__main__":
    # Example usage of the AlphaVantageProvider
    alpha_vantage_provider = AlphaVantageProvider()
    
    try:
        daily_data = alpha_vantage_provider.get_time_series_daily_data("AAPL")
        print("Daily data for AAPL:", daily_data)
    except Exception as e:
        print(f"Error fetching data: {e}")