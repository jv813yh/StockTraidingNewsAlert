# helper.py
# This module provides helper functions for summarizing daily stock data.
# It includes a method to summarize the daily time series data for a given stock symbol.
# Author: Vendel, GITHUB: jv813yh
# Date: 08/01/2025



class Helper:

    @staticmethod
    def sumarize_data(daily_data, company_name, stock_symbol):
        """Summarizes the daily time series data for a given stock symbol.
        Args:
            daily_data (dict): The daily time series data.
            company_name (str): The name of the company.
            stock_symbol (str): The stock symbol.
        Returns:
            Returns a summary of the daily data.
        """

        if not daily_data:
            return f"No data available for {company_name} ({stock_symbol})"

        returned_data = {stock_symbol: company_name}

        counter = 0
        # Print the fetched data
        print(f"Daily time series data for {company_name} ({stock_symbol}):")
        for date, data in daily_data.items():
            returned_data[date] = data
            print(f"{date}: {data}")
            counter += 1

            if counter >= 2:  # Limit to first 2 entries
                break