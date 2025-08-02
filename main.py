# main.py
# This script serves as the entry point for fetching 
# Author: Vendel, GITHUB: jv813yh
# Date: 08/01/2025
from builder import Builder

if __name__ == "__main__":

    builder_app = Builder()
    try:
        summary = builder_app.sumarize_stock_data()
        print("Summary of daily data:")
        print(summary)
    except Exception as e:
        print(f"An error occurred: {e}")