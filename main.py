# main.py
# This script serves as the entry point for fetching 
# Author: Vendel, GITHUB: jv813yh
# Date: 08/01/2025
from alpha_vantage_api import AlphaVantageProvider


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

if __name__ == "__main__":
    # Initialize the AlphaVantageProvider with your API key 
    api_key = 'F74BHY6LTAQHJ61K'
    provider = AlphaVantageProvider()

    try:
        # Fetch daily time series data for the specified stock symbol
        daily_data = provider.get_time_series_daily_data(STOCK)
        
        # Print the fetched data
        print(f"Daily time series data for {COMPANY_NAME} ({STOCK}):")
        for date, data in daily_data.items():
            print(f"{date}: {data}")
    
    except Exception as e:
        print(f"An error occurred: {e}")