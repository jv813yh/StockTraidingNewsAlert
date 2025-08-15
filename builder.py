# builder.py
# This module provides helper functions for summarizing daily stock data.
# It includes a method to summarize the daily time series data for a given stock symbol.
# Author: Vendel, GITHUB: jv813yh
# Date: 08/01/2025

import json
import datetime
from stock import Stock
from dotenv import load_dotenv, find_dotenv
import os


from alpha_vantage_api import AlphaVantageProvider
from hugging_face_api import HugginFaceProvider
from news_api import NewsAPIProvider
from twilio_provider import TwilioProvider
from yfinance_provider import YahooFinanceProvider

# Constants
REPO_ID = 'meta-llama/Llama-3.1-8B-Instruct:novita'
INPUT_FILE = 'stocks.json'
SATURDAY = 5
SUNDAY = 6

load_path = find_dotenv()
if load_path:
    load_dotenv(load_path)
# Fetching Twilio phone number from environment variables
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
if not PHONE_NUMBER:
    raise ValueError("PHONE_NUMBER not found in environment variables.")

class Builder:
    def __init__(self):
        self.alpha_vantage_provider = AlphaVantageProvider()
        self.hugging_face_provider = HugginFaceProvider()
        self.news_api_provider = NewsAPIProvider()
        self.twilio_provider = TwilioProvider()
        self.yahoo_finance_provider = YahooFinanceProvider()

    def sumarize_stocks_data(self):
        """Summarizes the daily time series data for a given stocks symbol from the input file.

        Returns:
            Returns a summary of the daily data.
        """
        try:
            daily_data_summaries = ""
            final_completion = ""
            stocks_list = self.load_stocks_from_json(INPUT_FILE)
            dates = []

            for stock in stocks_list:
                counter_days = 0
                # Fetch daily time series data for the stock symbol
                daily_data = self.yahoo_finance_provider.get_time_series_daily_data(stock.symbol)
                
                if not daily_data:
                    raise ValueError(f"No data found for stock symbol: {stock.symbol}")

                # Create a summary of the daily data
                daily_data_summaries += f"Summary for {stock.symbol} ({stock.company_name}):\n"
                for date, data in daily_data.items():
                    daily_data_summaries += f"Date: {date}, Open: {data['Open']}, Close: {data['Close']}\n"
                    dates.append(date)  
                    counter_days += 1

                    # We just want to summarize the data for two days
                    if counter_days == 2:
                        break

                # Get articles related to the stock symbol from the News API according to the dates
                news_articles = self.news_api_provider.get_news_articles(query=stock.symbol, company_name=stock.symbol, from_date=dates[0], to_date=dates[1])
                daily_data_summaries += "/n"+ news_articles
                # Get completion from the Hugging Face API
                stock_completion = self.hugging_face_provider.get_completion(repo_id=REPO_ID, prompt=daily_data_summaries)
                final_completion += f"\n{stock_completion}\n"
                daily_data_summaries = ""  # Reset daily data summaries for the next stock
                dates.clear()  # Clear dates for the next stock

            return final_completion
        except Exception as e:
            raise Exception(f"An error occurred while summarizing the stock data: {e}")

    def send_sms_notification(self, body, to=PHONE_NUMBER):
        """
        Sends an SMS notification using the Twilio provider.
        
        Args:
            to (str): The recipient's phone number.
            body (str): The content of the SMS message.
        
        Returns:
            Message: The sent message object.
        """
        try:
            return self.twilio_provider.sends_message_sms(to, body)
        except Exception as e:
            raise Exception(f"An error occurred while sending SMS notification: {e}")

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
    
    daily_data_summaries = builder.sumarize_stocks_data()
    print("Content of the file:", daily_data_summaries)
