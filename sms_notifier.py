import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

# load open weather map environment variables
load_dotenv(".env")

# twilio parameters
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
to_number = os.getenv("to_number")
from_number = os.getenv("from_number")


def format_articles(articles):
    message_body = """"""
    for headline, description in articles:
        message_body += f"\n"
        message_body += f"\nHeadline: {headline}"
        message_body += f"\nBrief: {description}"

    return message_body


def send_sms_update(STOCK, price_change, articles):
    global account_sid, auth_token
    client = Client(account_sid, auth_token)

    ticker_info_text = f"STOCK ALERT:\n\n{STOCK}: {price_change}%"
    message = ticker_info_text + format_articles(articles)

    message = client.messages.create(
        body=message,
        from_=from_number,
        to=to_number
    )
    print(message.status)
