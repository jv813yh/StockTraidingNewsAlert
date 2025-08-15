# yfinance_provider.py
# This module provides a class for fetching stock data using the Yahoo Finance API via yfinance library.
# Author: Vendel (original Alpha Vantage version adapted)
# Date: 08/14/2025

import yfinance as yf
import pandas as pd

class YahooFinanceProvider:
    def __init__(self):
        # Nothing special here – yfinance does not require API keys
        pass

    def get_time_series_daily_data(self, symbol: str, period: str = "2d"):
        """
        Fetches daily time series data for a given stock symbol using Yahoo Finance.
        Default period is 1 month, but can be '1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max'
        """
        try:
            ticker = yf.Ticker(symbol.upper())
            df = ticker.history(period=period, interval="1d")

            if df.empty:
                raise RuntimeError(f"No data returned for {symbol}")

            # Convert DataFrame to dict similar to Alpha Vantage style
            daily_data = {}
            for date, row in df.iterrows():
                daily_data[str(date.date())] = {
                    "Open": str(row["Open"]),
                    "High": str(row["High"]),
                    "Low": str(row["Low"]),
                    "Close": str(row["Close"]),
                    "Volume": str(int(row["Volume"]))
                }

            return daily_data

        except Exception as e:
            raise ConnectionError(f"Failed to fetch data for {symbol}: {e}")


if __name__ == "__main__":
    yahoo_provider = YahooFinanceProvider()
    try:
        daily_data = yahoo_provider.get_time_series_daily_data("AAPL")
        print("Daily data for AAPL:")
        for date, values in list(daily_data.items()):
            print(date, values)
    except Exception as e:
        print(f"Error fetching data: {e}")
