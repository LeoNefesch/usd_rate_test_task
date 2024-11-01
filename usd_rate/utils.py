import requests
from datetime import datetime, timedelta, timezone

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"  # Пример API


def fetch_current_usd_rate():
    try:
        response = requests.get(API_URL)
        data = response.json()
        usd_to_rub = data["rates"]["RUB"]
        current_time = datetime.now(timezone(timedelta(hours=3)))
        return usd_to_rub, current_time
    except Exception as e:
        print(f"Error fetching currency rate: {e}")
        return None, None

