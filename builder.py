# builder.py
# This module provides helper functions for summarizing daily stock data.
# It includes a method to summarize the daily time series data for a given stock symbol.
# Author: Vendel, GITHUB: jv813yh
# Date: 08/01/2025

import json
import datetime
from stock import Stock


from alpha_vantage_api import AlphaVantageProvider
from hugging_face_api import HugginFaceProvider
from news_api import NewsAPIProvider

# Constants
REPO_ID = 'meta-llama/Llama-3.1-8B-Instruct:novita'
INPUT_FILE = 'stocks.json'
SATURDAY = 5
SUNDAY = 6

class Builder:
    def __init__(self):
        self.alpha_vantage_provider = AlphaVantageProvider()
        self.hugging_face_provider = HugginFaceProvider()
        self.news_api_provider = NewsAPIProvider()

    def sumarize_stock_data(self):
        """Summarizes the daily time series data for a given stocks symbol from the input file.

        Returns:
            Returns a summary of the daily data.
        """
        try:
            daily_data_summaries = "Stock:\n"

            stocks_list = self.load_stocks_from_json(INPUT_FILE)
            dates = []

            for stock in stocks_list:
                counter_days = 0
                # Fetch daily time series data for the stock symbol
                daily_data = self.alpha_vantage_provider.get_time_series_daily_data(stock.symbol)
                
                if not daily_data:
                    raise ValueError(f"No data found for stock symbol: {stock.symbol}")

                # Create a summary of the daily data
                daily_data_summaries += f"Summary for {stock.symbol} ({stock.company_name}):\n"
                for date, data in daily_data.items():
                    daily_data_summaries += f"Date: {date}, Open: {data['1. open']}, Close: {data['4. close']}\n"
                    dates.append(date)  
                    counter_days += 1

                    # We just want to summarize the data for two days
                    if counter_days == 2:
                        break

                # Get articles related to the stock symbol from the News API according to the dates
                news_articles = self.news_api_provider.get_news_articles(stock.symbol, from_date=dates[0], to_date=dates[1])
                daily_data_summaries += "/n"+ str(news_articles[:3]) +"/n----------------------------\nStock:\n"

            # Get completion from the Hugging Face API
            final_completion = self.hugging_face_provider.get_completion(repo_id=REPO_ID, prompt=daily_data_summaries)
            return final_completion
        except Exception as e:
            raise Exception(f"An error occurred while summarizing the stock data: {e}")

    def create_dates(self):
        """
        Creates a date string for the current date and the day before.
        This is used to ensure that the date is not a weekend (Saturday or Sunday).

        Returns:
            tuple: A tuple containing the date string for the current date and the day before.
        
        """
        # Create a date string for the current date and the day before
        # This is used to ensure that the date is not a weekend (Saturday or Sunday)
        datetime_now_str, date_time_day_before_str = "", ""

        number_days = 1
        datetime_now = datetime.datetime.now()
        can_continue = True
        while(can_continue):
            if datetime_now.weekday() not in [SATURDAY, SUNDAY]:
                datetime_now_str = datetime.date.strftime(datetime_now, "%Y-%m-%d")

                date_time_day_before = datetime_now - datetime.timedelta(days=number_days)
                if date_time_day_before.weekday() != SATURDAY or date_time_day_before.weekday() != SUNDAY:
                    date_time_day_before_str = datetime.date.strftime(date_time_day_before, "%Y-%m-%d")
                    can_continue = False
                elif date_time_day_before.weekday() == SATURDAY:
                    print("Day before is SATURDAY, we have to get another day.")
                    number_days += 1
                    date_time_day_before = datetime_now - datetime.timedelta(days=number_days)
                    date_time_day_before_str = datetime.date.strftime(date_time_day_before, "%Y-%m-%d")
                    can_continue = False
                elif date_time_day_before.weekday() == SUNDAY:
                    print("Day before is SUNDAY, we have to get another day.")
                    number_days += 2
                    date_time_day_before = datetime_now - datetime.timedelta(days=number_days)
                    date_time_day_before_str = datetime.date.strftime(date_time_day_before, "%Y-%m-%d")
                    can_continue = False
            else:
                print("Today is weekend, we have to get another day.")
                datetime_now = datetime_now - datetime.timedelta(days=number_days)

        return datetime_now_str, date_time_day_before_str

    def load_stocks_from_json(self, file_path) -> list[Stock]:
        """
        
        """
        with open(file_path, 'r') as f:
            data = json.load(f)  

        stocks: list[Stock] = []
        for entry in data:
            try:
                symbol = entry["stock"]
                name = entry["company_name"]
            except KeyError:
                raise ValueError(f"No key in entry: {entry}")
            except Exception as e:
                raise Exception(f"An error occurred while loading stocks from JSON: {e}")

            stocks.append(Stock(symbol, name))
        return stocks

if __name__ == "__main__":

    # Example usage of the Builder class
    builder = Builder()
    
    daily_data_summaries = builder.sumarize_stock_data()
    print("Content of the file:", daily_data_summaries)