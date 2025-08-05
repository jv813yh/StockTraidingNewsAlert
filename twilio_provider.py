# twilipo_provider.py
# This module provides a provider for fetching news articles using the News API.
# Author: Vendel, GITHUB: jv813yh
# Date: 08/04/2025

from twilio.rest import Client
from dotenv import load_dotenv, find_dotenv
import os

dotenv_path = find_dotenv()
if dotenv_path:
    load_dotenv(dotenv_path)
# Fetching Twilio credentials from environment variables
TWILIO_ACCOUNT_SID =    os.getenv("TWILIO_ACCOUNT_SID")
if not TWILIO_ACCOUNT_SID:
    raise ValueError("TWILIO_ACCOUNT_SID not found in environment variables.")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
if not TWILIO_AUTH_TOKEN:
    raise ValueError("TWILIO_AUTH_TOKEN not found in environment variables.")
TWILIO_VIRTUAL_NUMBER = os.getenv("TWILIO_VIRTUAL_NUMBER")
if not TWILIO_VIRTUAL_NUMBER:
    raise ValueError("TWILIO_VIRTUAL_NUMBER not found in environment variables.")

class TwilioProvider:
    def __init__(self):
        self.twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def sends_message_sms(self, to, body):
        """
        Sends an SMS message using the Twilio client.
        
        Args:
            to (str): The recipient's phone number.
            body (str): The content of the SMS message.
        
        Returns:
            Message: The sent message object.
        """
        return self.twilio_client.messages.create(
            to=to,
            from_=TWILIO_VIRTUAL_NUMBER,
            body=body
        )

    @staticmethod
    def create_twilio_client():
        """
        Creates a Twilio client using the provided account SID and auth token.
        
        Returns:
            Client: An instance of the Twilio client.
        """
        return TwilioProvider().twilio_client
    

if __name__ == "__main__":
    # Example usage of the TwilioProvider to send an SMS message.
    twilio_provider = TwilioProvider()
    try:
        message = twilio_provider.sends_message_sms(
            to='+....',  # Replace with the recipient's phone number
            body='Hello from Twilio!'
        )
        print(f"Message sent successfully: {message.sid}")
    except Exception as e:
        print(f"An error occurred while sending the message: {e}")