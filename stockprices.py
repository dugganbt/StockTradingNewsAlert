import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

# load environment variables for API
load_dotenv(".env")
api_key_tiingo = os.getenv("api_key_tiingo")


def get_stock_price_last_two_days(ticker):
    global api_key_tiingo

    # Get the current date
    today = datetime.now()

    # Determine the day of the week (0=Monday, 1=Tuesday, ..., 6=Sunday)
    day_of_week = today.weekday()

    # Logic to compare the closing prices (there are none on the weekend).
    # Does not account for holidays
    if day_of_week == 0:  # Monday
        # Friday of last week
        start_date = today - timedelta(days=3)
        # Thursday of last week
        end_date = today - timedelta(days=4)
    elif day_of_week == 1:  # Tuesday
        # Friday of last week
        end_date = today - timedelta(days=4)
        # Yesterday (Monday)
        start_date = today - timedelta(days=1)
    else:
        # For other days, compare yesterday and the day before yesterday
        start_date = today - timedelta(days=1)
        end_date = today - timedelta(days=2)

    # Convert dates to the format "YYYY-MM-DD"
    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")

    print()

    parameters = {
        "startDate": end_date_str,
        "endDate": start_date_str,
        "format": "json",
        "resampleFreq": "daily",
        "token": api_key_tiingo
    }

    response = requests.get(
        url=f"https://api.tiingo.com/tiingo/daily/{ticker}/prices",
        params=parameters
    )

    adj_close_list = [(day_data["date"][:-14], day_data["adjClose"]) for day_data in response.json()]

    return adj_close_list


def calculate_price_change_percent(adj_close_list):
    day_before_yesterday = adj_close_list[0]
    yesterday = adj_close_list[1]

    # if >0 then it's an increase, if <0 then decrease
    ratio = round(1 - day_before_yesterday[1] / yesterday[1], 5) * 100

    return ratio
