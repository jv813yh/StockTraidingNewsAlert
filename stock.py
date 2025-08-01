# stock.py
# 
# Author: Vendel, GITHUB: jv813yh
# Date: 08/01/2025


class Stock:
    """
    A class representing a stock with its symbol and company name.
    
    Attributes:
        symbol (str): The stock symbol.
        company_name (str): The name of the company.
    """

    def __init__(self, symbol, company_name):
        """
        Initializes a Stock instance with the given symbol and company name.
        
        Args:
            symbol (str): The stock symbol.
            company_name (str): The name of the company.
        """
        self.symbol = symbol
        self.company_name = company_name

    def __repr__(self):
        return f"Stock(symbol='{self.symbol}', company_name='{self.company_name}')"