# news_api.py
# This module provides a class for interacting with the News API to fetch news articles.
# Author: Vendel, GITHUB: jv813yh
# Date: 08/01/2025

from http_client import HTTP_CLIENT_PROVIDER


API_KEY = 'f2b615d110e6454dacb9e17a1d3163d7'


class NewsAPIProvider:
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = "https://newsapi.org/v2/everything"

    def verify_api_key(self):
        """
        Verifies if the provided API key is valid by making a test request.
        Raises ValueError if the API key is empty.
        """
        if not self.api_key:
            raise ValueError("API key must not be empty")

    def get_news_articles(self, query, from_date=None, to_date=None):
        """
        Fetches news articles based on a query and optional date range.

        Args:
            query (str): The search query for news articles.
            from_date (str, optional): The start date for the news articles in 'YYYY-MM-DD' format.
            to_date (str, optional): The end date for the news articles in 'YYYY-MM-DD' format.
        Returns:
            list: A list of news articles matching the query and date range.
        """
        try:
            self.verify_api_key()
            
            params = {
                'q': query,
                'from': from_date,
                'to': to_date,
                'sortBy': 'popularity',
                'language': 'en',
                'apiKey': self.api_key
            }
            
            # Make the API request
            data_json = HTTP_CLIENT_PROVIDER.get(self.base_url, params=params)

            if 'articles' in data_json:
                return data_json['articles']
            
            return data_json
        except Exception as e:
            raise ConnectionError(f"An error occurred while fetching news articles: {e}")
        

if __name__ == "__main__":
    # Example usage of the NewsAPIProvider
    news_provider = NewsAPIProvider()
    
    try:
        articles = news_provider.get_news_articles(query="Tesla", from_date="2025-07-30", to_date="2025-07-31")
        print("Fetched news articles:")
        for article in articles:
            print(f"- {article['title']} ({article['publishedAt']})")


    except Exception as e:
        print(f"An error occurred: {e}")