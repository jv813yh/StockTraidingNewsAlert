# http_client.py
# This module provides a base class for making HTTP requests using the requests library.
# It includes methods for GET, POST, PUT, and DELETE requests.
# It is designed to be extended by other classes that require HTTP client functionality.
# Author: Vendel,
# Date: 08/01/2025

import requests


class HTTP_CLIENT_PROVIDER():
    """ 
        A base class for HTTP client providers.
        This class provides methods for making HTTP requests and handling responses.
    """

    @staticmethod
    def get(url, params=None, headers=None):
        """
        Makes an HTTP GET request to the specified URL with optional parameters and headers.
        
        Args:
            url (str): The URL to send the request to.
            params (dict, optional): Query parameters to include in the request.
            headers (dict, optional): Headers to include in the request.
        
        Returns:
            dict: The JSON response from the server.
        """
        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            raise ConnectionError(f"HTTP request failed: {e}")
        
    @staticmethod
    def post(url, data=None, headers=None):

        """
        Makes an HTTP POST request to the specified URL with optional data and headers.
        
        Args:
            url (str): The URL to send the request to.
            data (dict, optional): Data to include in the request body.
            headers (dict, optional): Headers to include in the request.
        
        Returns:
            dict: The JSON response from the server.
        """
        try:
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            raise ConnectionError(f"HTTP request failed: {e}")
        
    @staticmethod
    def put(url, data=None, headers=None):
        """
        Makes an HTTP PUT request to the specified URL with optional data and headers.
        
        Args:
            url (str): The URL to send the request to.
            data (dict, optional): Data to include in the request body.
            headers (dict, optional): Headers to include in the request.
        
        Returns:
            dict: The JSON response from the server.
        """
        try:
            response = requests.put(url, json=data, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            raise ConnectionError(f"HTTP request failed: {e}")
        
    @staticmethod
    def delete(url, headers=None):
        """
        Makes an HTTP DELETE request to the specified URL with optional headers.
        
        Args:
            url (str): The URL to send the request to.
            headers (dict, optional): Headers to include in the request.
        
        Returns:
            dict: The JSON response from the server.
        """
        try:
            response = requests.delete(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            raise ConnectionError(f"HTTP request failed: {e}")