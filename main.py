from stockprices import get_stock_price_last_two_days, calculate_price_change_percent
from news import get_n_articles_last_two_days
from sms_notifier import send_sms_update

STOCK = "TSLA"
search_term = "Tesla"
from_date = "2024-05-20"


stock_price_last_two_days = get_stock_price_last_two_days(STOCK)
price_change = calculate_price_change_percent(stock_price_last_two_days)

if price_change > 5 or price_change < -5:
    articles = get_n_articles_last_two_days(search_term=search_term, number_of_articles=3)
    send_sms_update(STOCK, price_change, articles)
else:
    print(f"No news alert sent: {STOCK}: {price_change}")

