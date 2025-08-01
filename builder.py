# builder.py
# This module provides helper functions for summarizing daily stock data.
# It includes a method to summarize the daily time series data for a given stock symbol.
# Author: Vendel, GITHUB: jv813yh
# Date: 08/01/2025

import json

from alpha_vantage_api import AlphaVantageProvider
from hugging_face_api import HugginFaceProvider
from news_api import NewsAPIProvider

# Constants
REPO_ID = 'meta-llama/Llama-3.1-8B-Instruct:novita'
INPUT_FILE = 'stocks.json'

class Builder:
    def __init__(self):
        self.alpha_vantage_provider = AlphaVantageProvider()
        self.hugging_face_provider = HugginFaceProvider()
        self.news_api_provider = NewsAPIProvider()

    def sumarize_data(self, 
                      company_name, 
                      stock_symbol):
        """Summarizes the daily time series data for a given stock symbol.
        Args:
            company_name (str): The name of the company.
            stock_symbol (str): The stock symbol.
        Returns:
            Returns a summary of the daily data.
        """
    def get_content_file(self, 
                        file_path):
        """Reads the content of a file.
        Args:
            file_path (str): The path to the file.
        Returns:
            str: The content of the file.
        """
        with open(file_path, 'r') as file:
            content = json.loads(file.read())

        return content
    
    def build_jobs(self):
        """Builds jobs for summarizing stock data and fetching news articles."""
        # Example usage of the AlphaVantageProvider
        try:
            daily_data = self.alpha_vantage_provider.get_time_series_daily_data("TSLA")
            print(f"Daily time series data for Tesla Inc (TSLA): {daily_data}")
        except Exception as e:
            print(f"An error occurred while fetching daily data: {e}")

        # Example usage of the NewsAPIProvider
        try:
            news_articles = self.news_api_provider.get_news_articles("Tesla", from_date="2025-01-01", to_date="2025-01-31")
            print(f"News articles for Tesla: {news_articles}")
        except Exception as e:
            print(f"An error occurred while fetching news articles: {e}")

if __name__ == "__main__":
    # Example usage of the Builder class
    builder = Builder()
    
    content = builder.get_content_file(INPUT_FILE)
    print("Content of the file:", content)