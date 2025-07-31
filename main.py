from alphavantage_provider import AlphaVantageProvider


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

if __name__ == "__main__":
    # Initialize the AlphaVantageProvider with your API key 
    api_key = 'F74BHY6LTAQHJ61K'
    provider = AlphaVantageProvider(api_key)

    try:
        # Fetch daily time series data for the specified stock symbol
        daily_data = provider.get_time_series_daily_data(STOCK)
        
        # Print the fetched data
        print(f"Daily time series data for {COMPANY_NAME} ({STOCK}):")
        for date, data in daily_data.items():
            print(f"{date}: {data}")
    
    except Exception as e:
        print(f"An error occurred: {e}")