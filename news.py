import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

# load environment variables for API
load_dotenv(".env")
api_key_news = os.getenv("api_key_news")

sort_by = "popularity"


def extract_title_and_description(list_of_articles):
    return [(article['title'], article['description']) for article in list_of_articles]


def get_n_articles_last_two_days(search_term="weather", number_of_articles=3):
    global api_key_news, sort_by

    # Get the current date
    today = datetime.now()

    # Calculate the day before yesterday's date
    day_before_yesterday = today - timedelta(days=4)

    # Convert dates to the format "YYYY-MM-DD"
    day_before_yesterday_str = day_before_yesterday.strftime("%Y-%m-%d")

    params = {
        'q': search_term,
        'from': day_before_yesterday_str,
        'sortBy': sort_by,
        'apiKey': api_key_news
    }

    url = 'https://newsapi.org/v2/everything'

    response = requests.get(url, params)

    return extract_title_and_description(response.json()["articles"][:number_of_articles])
