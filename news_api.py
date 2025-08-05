# news_api.py
# This module provides a class for interacting with the News API to fetch news articles.
# Author: Vendel, GITHUB: jv813yh
# Date: 08/01/2025

from http_client import HTTP_CLIENT_PROVIDER
from dotenv import load_dotenv, find_dotenv
import os


dotenv_path = find_dotenv()
if dotenv_path:
    load_dotenv(dotenv_path)
# Fetching News API key from environment variables
API_KEY = os.getenv("NEWS_API_KEY")
if not API_KEY:
    raise ValueError("NEWS_API_KEY not found in environment variables.")


class NewsAPIProvider:
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = "https://newsapi.org/v2/everything"

    def create_correct_format_articles(self, articles:dict):
        """
        Converts the articles to a correct format for further processing.
        
        Args:
            articles (dict): dict of articles to be formatted.
        
        Returns:
            string: formatted data of articles.
        """
        if "articles" not in articles:
            raise ValueError("No articles found in the response.")
        if len(articles["articles"]) == 0:
            raise ValueError("No articles found for the given query.")
        formatted_articles = ""
        counter = 0
        for article in articles["articles"]:
            formatted_articles += f"Title: {article['title']}\nContent: {article['content']}\nPublished At: {article['publishedAt']}\n"
            counter += 1
            if counter == 3:  # Limit to 3 articles
                break
        
        return formatted_articles

    def get_news_articles(self, query, company_name, from_date=None, to_date=None):
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
            
            params = {
                #'q': query,
                'from': from_date,
                'to': to_date,
                'sortBy': 'popularity',
                'language': 'en',
                'qInTitle': company_name,
                'apiKey': self.api_key
            }
            
            # Make the API request
            data_json = HTTP_CLIENT_PROVIDER.get(self.base_url, params=params)

            if 'articles' in data_json:
                # Format the articles for further processing
                formatted_articles =self.create_correct_format_articles(data_json)
                return formatted_articles
            
            return data_json
        except Exception as e:
            raise ConnectionError(f"An error occurred while fetching news articles: {e}")
        

if __name__ == "__main__":
    # Example usage of the NewsAPIProvider
    news_provider = NewsAPIProvider()
    
    try:
        articles = news_provider.get_news_articles(query="Tesla", company_name="", from_date="2025-07-30", to_date="2025-07-31")
        print("Fetched news articles:")


    except Exception as e:
        print(f"An error occurred: {e}")